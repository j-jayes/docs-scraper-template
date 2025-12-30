# Usage Example

This file demonstrates how to use the docs-scraper-template in your own repository.

## Example 1: Scraping Google ADK Documentation

1. Edit `.github/agent-docs/config.yaml`:

```yaml
docs_to_scrape:
  - url: "https://google.github.io/adk-docs/"
    name: "adk-docs"
```

2. Run the scraper:
   - Via GitHub Actions: Go to Actions → Scrape Documentation → Run workflow
  - Or locally: `python .github/agent-docs/scraper.py`

3. The scraped reference content will be saved to `.github/agent-docs/reference/adk-docs/`

## Example 2: Scraping Multiple Documentation Sites

```yaml
docs_to_scrape:
  - url: "https://google.github.io/adk-docs/"
    name: "adk-docs"
  
  - url: "https://docs.python.org/3/"
    name: "python-docs"
  
  - url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/"
    name: "mdn-javascript"
```

Each site will be scraped into its own directory:
- `.github/agent-docs/reference/adk-docs/`
- `.github/agent-docs/reference/python-docs/`
- `.github/agent-docs/reference/mdn-javascript/`

## Running Locally

```bash
# Install dependencies
pip install pyyaml html2text

# Run the scraper
cd your-repository
python .github/agent-docs/scraper.py
```

## Testing with a Small Site

For testing, you can use a small documentation site:

```yaml
docs_to_scrape:
  - url: "https://httpbin.org/"
    name: "test-httpbin"
```

## Important Notes

### Source Types (Auto-Detect + Override)

The scraper supports two kinds of sources:

- **Website**: any normal docs site (default for non-GitHub URLs)
  - Writes `raw/` HTML and converted `md/` Markdown.
- **GitHub repo**: `https://github.com/<owner>/<repo>` (auto-detected)
  - Downloads the entire repo via `codeload.github.com` and extracts it to `repo/`.

You can override detection per entry:

```yaml
docs_to_scrape:
  - url: "https://github.com/example/acme"
    name: "acme"
    type: github_repo

  - url: "https://example.com/docs/"
    name: "example-docs"
    type: website
```

### Example 3: Scraping a GitHub Repository (Full Repo)

```yaml
docs_to_scrape:
  - url: "https://github.com/example/acme"
    name: "acme"
    # Optional ref override (branch/tag/SHA). If omitted, the scraper will try HEAD/main/master.
    ref: "main"
```

Output:
- `.github/agent-docs/reference/acme/repo/` (full extracted repo)
- `.github/agent-docs/reference/acme/llms-full.txt` (agent-friendly aggregate)

### Example 4: Website Output Layout

For websites, output is:
- `.github/agent-docs/reference/<name>/raw/` (raw HTML)
- `.github/agent-docs/reference/<name>/md/` (Markdown conversions)
- `.github/agent-docs/reference/<name>/llms-full.txt`


1. **Base URL Path**: The scraper only follows links that start with the same base URL path
   - ✅ Good: `https://example.com/docs/` will scrape all pages under `/docs/`
   - ❌ Won't work: It won't follow links to `https://example.com/blog/`

2. **Large Sites**: By default, limited to 1000 pages. You can raise it per entry:
  ```yaml
  docs_to_scrape:
    - url: "https://example.com/docs/"
     name: "example-docs"
     max_pages: 2000
  ```

3. **JavaScript Content**: This scraper downloads static HTML only. Sites that load content via JavaScript won't be fully scraped.

4. **Rate Limiting**: The scraper doesn't include delays. For large sites, consider adding `time.sleep()` between requests.
