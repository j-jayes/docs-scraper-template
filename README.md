# docs-scraper-template

A reusable template for scraping documentation websites and maintaining local copies. This template can be easily copied into any repository to automatically scrape and store documentation.

## Features

- 🚀 Simple configuration via YAML
- 📦 No virtual environment required - uses only standard Python libraries + PyYAML
- 🔄 Automatic GitHub Actions workflow
- 🌐 Recursively scrapes all pages from a documentation root URL
- 🧩 Autodetects website vs GitHub repo sources (with override)
- 📝 Converts HTML → Markdown for agent-friendly reading
- 📁 Organizes scraped reference docs in `.github/agent-docs/reference/<docs-name>/`
- ⏰ Runs automatically on schedule (weekly by default) or manually

## Quick Start

### 1. Copy Template Files

Copy the `.github/` directory from this template to your repository:

```bash
# If you're in your target repository
cp -r /path/to/docs-scraper-template/.github .
```

### 2. Configure Documentation URLs

Edit `.github/agent-docs/config.yaml` to specify which documentation sources you want to scrape:

```yaml
docs_to_scrape:
  - url: "https://google.github.io/adk-docs/"
    name: "adk-docs"
  
  - url: "https://docs.python.org/3/"
    name: "python-docs"
```

Each entry needs:
- `url`: The documentation source (website URL or GitHub repo URL)
- `name`: A folder name where the reference will be saved (creates `.github/agent-docs/reference/<name>/`)

### 3. Run the Scraper

#### Option A: Run via GitHub Actions (Recommended)

1. Commit and push the `.github/` directory to your repository
2. Go to the "Actions" tab in your GitHub repository
3. Select "Scrape Documentation" workflow
4. Click "Run workflow"

The workflow will:
- Automatically scrape all configured documentation sites
- Save the content to `.github/<name>/` directories
- Commit and push the changes

#### Option B: Run Locally

```bash
# Install dependencies
pip install pyyaml html2text

# Run the scraper
python .github/agent-docs/scraper.py
```

## How It Works

1. **Configuration**: The scraper reads `.github/agent-docs/config.yaml` to get the list of documentation sources
2. **Recursive Scraping**: For each URL, it:
   - Downloads the page content
   - Extracts all links on the page
   - Follows links that belong to the same documentation site
   - Saves HTML pages with their original directory structure
3. **Local Storage**: All scraped reference content is saved to `.github/agent-docs/reference/<name>/` where `<name>` matches the configuration
4. **Automatic Updates**: The GitHub Actions workflow runs weekly (or on-demand) to keep docs up-to-date

## Workflow Schedule

The scraper runs automatically:
- **Weekly**: Every Monday at 00:00 UTC
- **On Config Changes**: When `.github/agent-docs/config.yaml` is modified
- **Manual**: Via GitHub Actions "Run workflow" button

To change the schedule, edit `.github/workflows/scrape-docs.yml` and modify the `cron` expression.

## File Structure

```
your-repository/
└── .github/
  ├── agent-docs/
  │   ├── config.yaml          # Configuration file
  │   ├── scraper.py           # Main scraper script
  │   ├── USAGE.md             # Usage examples
  │   ├── QUICKSTART.md        # Quick start
  │   └── reference/           # Generated reference content (auto-generated)
  │       └── <docs-name>/
  │           ├── raw/          # Raw HTML (for websites)
  │           ├── md/           # Markdown conversions (for websites)
  │           ├── repo/         # Extracted GitHub repo (for github.com sources)
  │           ├── llms.txt
  │           └── llms-full.txt
    ├── workflows/
    │   └── scrape-docs.yml      # GitHub Actions workflow

```

## Customization

### Adjust Maximum Pages

By default, the scraper limits to 1000 pages per website. To change this, edit `.github/agent-docs/scraper.py`:

```python
self._scrape_recursive(url, url, output_dir, max_pages=2000)  # Increase limit
```

### Change Workflow Trigger

Edit `.github/workflows/scrape-docs.yml` to customize when scraping runs:

```yaml
on:
  workflow_dispatch:  # Manual trigger
  schedule:
    - cron: '0 0 * * 1'  # Weekly on Monday at 00:00 UTC
  push:
    paths:
      - '.github/agent-docs/config.yaml'  # When config changes
```

## Requirements

- Python 3.x
- PyYAML and html2text (installed automatically by GitHub Actions, or via `pip install pyyaml html2text`)

No virtual environment needed! The script uses only standard library modules plus PyYAML + html2text.

## Troubleshooting

### Scraper doesn't follow certain links

- Some documentation sites use JavaScript to load content, which this scraper won't capture
- The scraper only follows links within the same base URL path

### Rate limiting or blocked requests

- The scraper includes a User-Agent header to avoid basic bot detection
- Add delays between requests if needed (modify `scraper.py`)

### Large documentation sites

- Increase the `max_pages` limit if you need to scrape more than 1000 pages
- The scraper will stop at the limit to prevent excessive downloads

## License

This is a template - use it however you like!