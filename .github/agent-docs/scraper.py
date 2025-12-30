#!/usr/bin/env python3
"""Documentation Scraper

Purpose
  Keep a repository-local, up-to-date copy of external reference material so
  coding agents can rely on it during development.

Layout
  - This script and its configuration live under `.github/agent-docs/`.
  - Generated reference outputs are written to `.github/agent-docs/reference/`.

Supported sources
  - Normal websites: recursively crawl HTML pages under a root URL, saving:
      - raw HTML under `reference/<name>/raw/`
      - Markdown conversions under `reference/<name>/md/`
      - `llms.txt` and `llms-full.txt` aggregates
  - GitHub repositories: autodetected for `github.com/...` URLs, downloaded via
    `codeload.github.com` ZIP and extracted under `reference/<name>/repo/`.

Config
  docs_to_scrape entries support:
    - url (required)
    - name (required)
    - type: auto (default) | website | github_repo
    - max_pages: website crawl limit (default 1000)
    - ref / github.ref: optional GitHub ref override (branch/tag/SHA)

Notes
  - GitHub repo mode defaults to downloading the whole repo (for code context).
  - Website mode stores both raw HTML and derived Markdown.
"""

from __future__ import annotations

import os
import shutil
import sys
import argparse
import tempfile
import urllib.parse
import urllib.request
import zipfile
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable, List, Optional, Set, TextIO, Tuple

import yaml


USER_AGENT = "docs-scraper-template/1.1 (+https://github.com/)"


def _script_root() -> Path:
    return Path(__file__).resolve().parent


def _reference_root() -> Path:
    return _script_root() / "reference"


class LinkExtractor(HTMLParser):
    """Extract links from HTML content."""

    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base_url = base_url
        self.links: Set[str] = set()

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        if tag.lower() != "a":
            return

        href: Optional[str] = None
        for attr, value in attrs:
            if attr.lower() == "href":
                href = value
                break

        if not href:
            return

        href = href.strip()
        if not href or href.startswith("#"):
            return
        if href.startswith(("mailto:", "tel:", "javascript:")):
            return

        absolute_url = urllib.parse.urljoin(self.base_url, href)
        self.links.add(absolute_url)


@dataclass(frozen=True)
class ScrapeTarget:
    name: str
    url: str
    source_type: str  # "website" | "github_repo"
    max_pages: int = 1000
    github_ref: Optional[str] = None


class DocsScraper:
    def __init__(self, config_path: Path) -> None:
        self.config_path = config_path
        self.targets = self._load_config(config_path)
        self.visited_urls: Set[str] = set()
        self._reached_page_limit = False

    def _load_config(self, config_path: Path) -> List[ScrapeTarget]:
        try:
            with config_path.open("r", encoding="utf-8") as f:
                loaded = yaml.safe_load(f)

            config_data = loaded if isinstance(loaded, dict) else {}
            entries = config_data.get("docs_to_scrape", []) or []
            if not isinstance(entries, list):
                raise ValueError("docs_to_scrape must be a list")

            targets: List[ScrapeTarget] = []
            for entry in entries:
                if not isinstance(entry, dict):
                    continue

                url = (entry.get("url") or "").strip()
                name = (entry.get("name") or "").strip()
                if not url or not name:
                    continue

                override = (entry.get("type") or entry.get("source_type") or "auto").strip().lower()
                source_type = self._detect_source_type(url) if override in ("", "auto") else override
                if source_type not in ("website", "github_repo"):
                    print("Skipping {}: unsupported type '{}'".format(name, source_type))
                    continue

                max_pages = int(entry.get("max_pages") or 1000)

                github_ref = entry.get("ref")
                github_block = entry.get("github")
                if not github_ref and isinstance(github_block, dict):
                    github_ref = github_block.get("ref")

                targets.append(
                    ScrapeTarget(
                        name=name,
                        url=url,
                        source_type=source_type,
                        max_pages=max_pages,
                        github_ref=github_ref,
                    )
                )

            return targets
        except FileNotFoundError:
            print("Error: Config file not found at {}".format(config_path))
            sys.exit(1)
        except Exception as e:
            print("Error loading config: {}".format(e))
            sys.exit(1)

    def _detect_source_type(self, url: str) -> str:
        parts = urllib.parse.urlparse(url)
        netloc = parts.netloc.lower()
        if parts.scheme in ("http", "https") and netloc in ("github.com", "www.github.com"):
            path_parts = [p for p in parts.path.split("/") if p]
            if len(path_parts) >= 2:
                return "github_repo"
        return "website"

    def _request(self, url: str) -> urllib.request.Request:
        return urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    def _download_bytes(self, url: str, timeout_seconds: int = 30) -> Optional[bytes]:
        try:
            with urllib.request.urlopen(self._request(url), timeout=timeout_seconds) as response:
                return response.read()
        except Exception as e:
            print("Error downloading {}: {}".format(url, e))
            return None

    def _is_same_domain(self, url: str, base_url: str) -> bool:
        url_parts = urllib.parse.urlparse(url)
        base_parts = urllib.parse.urlparse(base_url)
        return (
            url_parts.scheme == base_parts.scheme
            and url_parts.netloc == base_parts.netloc
            and url_parts.path.startswith(base_parts.path)
        )

    def _relative_url_path(self, url: str, base_url: str) -> str:
        url_parsed = urllib.parse.urlparse(url)
        base_parsed = urllib.parse.urlparse(base_url)

        url_path = url_parsed.path
        base_path = base_parsed.path
        if url_path.startswith(base_path):
            relative_path = url_path[len(base_path) :]
        else:
            relative_path = url_path

        relative_path = relative_path.lstrip("/")
        if not relative_path or relative_path.endswith("/"):
            relative_path = os.path.join(relative_path, "index.html")
        if not os.path.splitext(relative_path)[1]:
            relative_path = relative_path + ".html"
        return relative_path

    def _extract_links(self, html_content: bytes, base_url: str) -> Set[str]:
        try:
            parser = LinkExtractor(base_url)
            parser.feed(html_content.decode("utf-8", errors="ignore"))
            return parser.links
        except Exception as e:
            print("Error extracting links: {}".format(e))
            return set()

    def _html_to_markdown(self, html_bytes: bytes) -> str:
        try:
            import html2text  # type: ignore

            converter = html2text.HTML2Text()
            converter.body_width = 0
            converter.ignore_links = False
            converter.ignore_images = True
            converter.ignore_emphasis = False
            html_text = html_bytes.decode("utf-8", errors="ignore")
            return converter.handle(html_text)
        except ModuleNotFoundError:
            print("Missing dependency 'html2text'. Install it with: pip install html2text")
            raise

    def _scrape_website_recursive(
        self,
        url: str,
        base_url: str,
        raw_root: Path,
        md_root: Path,
        llms_index_file: TextIO,
        llms_full_file: TextIO,
        max_pages: int,
    ) -> None:
        clean_url = url.split("#")[0].split("?")[0]
        if not clean_url:
            return

        if self._reached_page_limit:
            return
        if clean_url in self.visited_urls:
            return
        if len(self.visited_urls) >= max_pages:
            self._reached_page_limit = True
            print("Reached maximum page limit ({})".format(max_pages))
            return
        if not self._is_same_domain(clean_url, base_url):
            return

        self.visited_urls.add(clean_url)
        print("Scraping [{}]: {}".format(len(self.visited_urls), clean_url))

        content = self._download_bytes(clean_url)
        if not content:
            return

        rel_path = self._relative_url_path(clean_url, base_url)
        raw_path = raw_root / rel_path
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        raw_path.write_bytes(content)

        md_rel = os.path.splitext(rel_path)[0] + ".md"
        md_path = md_root / md_rel
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_text = self._html_to_markdown(content)
        md_path.write_text(md_text, encoding="utf-8")

        llms_index_file.write("{}\tmd/{}\n".format(clean_url, md_rel.replace(os.sep, "/")))
        llms_full_file.write("\n\n" + ("=" * 80) + "\n")
        llms_full_file.write("URL: {}\n".format(clean_url))
        llms_full_file.write("LOCAL_MD: md/{}\n".format(md_rel.replace(os.sep, "/")))
        llms_full_file.write(("=" * 80) + "\n\n")
        llms_full_file.write(md_text)

        url_path = urllib.parse.urlparse(clean_url).path
        file_ext = os.path.splitext(url_path)[1].lower()
        is_html = file_ext in ("", ".html", ".htm") or url_path.endswith("/")
        if not is_html:
            return

        for link in self._extract_links(content, clean_url):
            next_clean = link.split("#")[0].split("?")[0]
            if next_clean and self._is_same_domain(next_clean, base_url):
                self._scrape_website_recursive(
                    next_clean,
                    base_url,
                    raw_root,
                    md_root,
                    llms_index_file,
                    llms_full_file,
                    max_pages,
                )

    def _parse_github_repo(self, url: str) -> Tuple[str, str, Optional[str]]:
        parts = urllib.parse.urlparse(url)
        path_parts = [p for p in parts.path.split("/") if p]
        if len(path_parts) < 2:
            raise ValueError("Invalid GitHub repo URL: {}".format(url))

        owner, repo = path_parts[0], path_parts[1]
        if repo.endswith(".git"):
            repo = repo[: -len(".git")]

        # Support URLs like /owner/repo/tree/<ref>/...
        ref: Optional[str] = None
        if len(path_parts) >= 4 and path_parts[2] == "tree":
            ref = path_parts[3]

        return owner, repo, ref

    def _try_download_github_zip(self, owner: str, repo: str, refs: Iterable[str]) -> Tuple[bytes, str]:
        last_error: Optional[Exception] = None
        for ref in refs:
            zip_url = "https://codeload.github.com/{}/{}/zip/{}".format(owner, repo, ref)
            try:
                with urllib.request.urlopen(self._request(zip_url), timeout=60) as response:
                    return response.read(), ref
            except Exception as e:
                last_error = e
                continue
        raise RuntimeError("Failed to download GitHub ZIP for {}/{}: {}".format(owner, repo, last_error))

    def _is_text_file(self, path: Path, max_bytes: int) -> bool:
        if path.is_dir():
            return False

        try:
            size = path.stat().st_size
        except OSError:
            return False

        if size == 0 or size > max_bytes:
            return False

        ext = path.suffix.lower()
        if ext in (
            ".png",
            ".jpg",
            ".jpeg",
            ".gif",
            ".webp",
            ".ico",
            ".pdf",
            ".zip",
            ".gz",
            ".tgz",
            ".7z",
            ".exe",
            ".dll",
            ".so",
            ".dylib",
            ".bin",
            ".woff",
            ".woff2",
            ".ttf",
            ".eot",
            ".mp4",
            ".mp3",
            ".mov",
        ):
            return False

        try:
            data = path.read_bytes()
            data.decode("utf-8")
            return True
        except Exception:
            return False

    def _write_repo_llms(self, repo_root: Path, out_dir: Path, max_file_bytes: int = 512_000) -> None:
        llms_txt = out_dir / "llms.txt"
        llms_full = out_dir / "llms-full.txt"

        repo_root_resolved = repo_root.resolve()

        files: List[Path] = []
        for path in repo_root.rglob("*"):
            if ".git" in path.parts:
                continue
            if path.is_dir():
                continue
            if self._is_text_file(path, max_bytes=max_file_bytes):
                files.append(path)

        files.sort(key=lambda p: str(p).lower())

        with llms_txt.open("w", encoding="utf-8") as index_f, llms_full.open("w", encoding="utf-8") as full_f:
            index_f.write("# Repo file index (text files)\n")
            index_f.write("# Root: {}\n".format(repo_root))
            index_f.write("# Columns: relative_path\n\n")

            full_f.write("Repo: {}\n".format(repo_root.name))
            full_f.write("Root: {}\n".format(repo_root))
            full_f.write("\n" + ("=" * 80) + "\n")

            for path in files:
                rel = path.resolve().relative_to(repo_root_resolved)
                rel_str = str(rel).replace(os.sep, "/")
                index_f.write(rel_str + "\n")

                full_f.write("\n\n" + ("=" * 80) + "\n")
                full_f.write("FILE: {}\n".format(rel_str))
                full_f.write(("=" * 80) + "\n\n")
                full_f.write(path.read_text(encoding="utf-8", errors="ignore"))

    def scrape_target(self, target: ScrapeTarget, max_pages_override: Optional[int] = None) -> None:
        out_dir = _reference_root() / target.name
        out_dir.mkdir(parents=True, exist_ok=True)

        print("\n{}".format("=" * 80))
        print("Scraping: {}".format(target.name))
        print("URL: {}".format(target.url))
        print("TYPE: {}".format(target.source_type))
        print("OUTPUT: {}".format(out_dir))
        print("{}\n".format("=" * 80))

        if target.source_type == "website":
            raw_root = out_dir / "raw"
            md_root = out_dir / "md"
            raw_root.mkdir(parents=True, exist_ok=True)
            md_root.mkdir(parents=True, exist_ok=True)

            self.visited_urls = set()
            self._reached_page_limit = False
            llms_txt = out_dir / "llms.txt"
            llms_full = out_dir / "llms-full.txt"
            with llms_txt.open("w", encoding="utf-8") as index_f, llms_full.open("w", encoding="utf-8") as full_f:
                index_f.write("# Website page index\n")
                index_f.write("# Columns: url\tlocal_md\n\n")

                full_f.write("Website: {}\n".format(target.url))
                full_f.write("Output: {}\n\n".format(out_dir))

                self._scrape_website_recursive(
                    target.url,
                    target.url,
                    raw_root,
                    md_root,
                    index_f,
                    full_f,
                    max_pages=max_pages_override if max_pages_override is not None else target.max_pages,
                )

            print("\nCompleted scraping {}".format(target.name))
            print("Total pages downloaded: {}".format(len(self.visited_urls)))
            return

        if target.source_type == "github_repo":
            owner, repo, ref_from_url = self._parse_github_repo(target.url)
            ref_candidates: List[str] = []
            if target.github_ref:
                ref_candidates.append(str(target.github_ref))
            if ref_from_url:
                ref_candidates.append(ref_from_url)
            ref_candidates.extend(["HEAD", "main", "master"])

            zip_bytes, used_ref = self._try_download_github_zip(owner, repo, refs=ref_candidates)
            print("Downloaded ZIP for {}/{} (ref={})".format(owner, repo, used_ref))

            repo_out = out_dir / "repo"
            if repo_out.exists():
                shutil.rmtree(repo_out)

            with tempfile.TemporaryDirectory() as td:
                temp_dir = Path(td)
                zip_path = temp_dir / "repo.zip"
                zip_path.write_bytes(zip_bytes)

                extract_dir = temp_dir / "unzipped"
                extract_dir.mkdir(parents=True, exist_ok=True)
                with zipfile.ZipFile(str(zip_path)) as zf:
                    zf.extractall(str(extract_dir))

                children = [p for p in extract_dir.iterdir() if p.is_dir()]
                if len(children) != 1:
                    raise RuntimeError("Unexpected ZIP layout for {}/{}".format(owner, repo))
                extracted_root = children[0]
                shutil.copytree(extracted_root, repo_out)

            self._write_repo_llms(repo_out, out_dir)
            print("\nCompleted scraping {}".format(target.name))
            print("Repo extracted to: {}".format(repo_out))
            print("LLM bundles: {}, {}".format(out_dir / "llms.txt", out_dir / "llms-full.txt"))
            return

        raise RuntimeError("Unsupported target type: {}".format(target.source_type))

    def scrape_all(self, only_names: Optional[Set[str]] = None, max_pages_override: Optional[int] = None) -> None:
        if not self.targets:
            print("No documentation sources configured in config.yaml")
            return

        _reference_root().mkdir(parents=True, exist_ok=True)
        for target in self.targets:
            if only_names and target.name not in only_names:
                continue
            self.scrape_target(target, max_pages_override=max_pages_override)


def main() -> None:
    script_dir = _script_root()
    config_path = script_dir / "config.yaml"

    print("Documentation Scraper")
    print("=" * 80)
    print("Config file: {}".format(config_path))
    print("Output root: {}".format(_reference_root()))
    print("")

    parser = argparse.ArgumentParser(description="Scrape configured docs sources into .github/agent-docs/reference")
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        help="Scrape only the named entry from config.yaml (can be repeated)",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Override website max_pages for this run (useful for quick testing)",
    )
    args = parser.parse_args()

    only_names = set(args.only) if args.only else None

    scraper = DocsScraper(config_path)
    scraper.scrape_all(only_names=only_names, max_pages_override=args.max_pages)
    print("\nScraping completed!")


if __name__ == "__main__":
    main()
