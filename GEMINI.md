# Pokémon TCG Deck Analysis

A Python-based tool for scraping, analyzing, and reporting on Pokémon Trading Card Game (TCG) deck trends from Japanese tournaments on [Limitless TCG](https://limitlesstcg.com/tournaments/jp).

## Project Overview

This project automates the collection of competitive tournament data and generates detailed reports on deck archetypes. It helps identify meta "skeleton" lists and common tech choices by calculating card distribution frequencies.

### Architecture
- **Scraper (`src/scrape.py`):** Fetches tournament results and decklists. Implements a canonicalization cache to handle multiple prints of the same card.
- **Analyzer (`src/analyze.py`):** Processes the scraped CSV data, calculates card counts and distributions, and generates static HTML reports using Jinja2 templates.
- **Data Storage (`src/data/`):** Stores raw tournament data in CSV format and a JSON cache for card URL canonicalization.
- **Static Site (`docs/`):** The generated analytics dashboard, hosted via GitHub Pages.

## Tech Stack
- **Python 3.12+**
- **[uv](https://github.com/astral-sh/uv)** for environment management.
- **Scraping:** `requests`, `beautifulsoup4`, `tenacity`.
- **Templating:** `Jinja2`.

## Building and Running

### Setup
```bash
uv sync
```

### Data Update
To fetch the latest tournament results and append them to the local dataset:
```bash
uv run src/scrape.py
```

### Report Generation
To analyze the current dataset and update the HTML reports:
```bash
uv run src/analyze.py
```

## Development Conventions

### Card Canonicalization (First-Encountered Algorithm)
To prevent duplicate card entries in reports due to different set prints (e.g., Poké Pad), the scraper uses a mapping strategy:
- **Cache:** `src/data/card_cache.json` stores mappings.
- **Logic:** For any card, check the `table.card-prints-versions` on its Limitless page. All listed versions are mapped to the *first* URL encountered for that card.
- **Storage:** Cache keys are stored as minimal path strings (e.g., `SVI/169`) by stripping the `https://limitlesstcg.com/cards/` prefix.

### Image CDN Logic
Card images are fetched from the Limitless CDN. The logic branches based on whether the card is a Japanese version:

| Feature | Japanese Cards (`/jp/` in URL) | Standard (English) Cards |
| :--- | :--- | :--- |
| **CDN Path** | `.../tpc/[SET]/...` | `.../tpci/[SET]/...` |
| **File Suffix** | `_R_JP.png` | `_R_EN.png` |
| **Number Padding** | None (e.g., `79`) | 3-digit zero-padded (e.g., `079`) |
| **Query Params** | Stripped for image URL | Stripped for image URL |

### UI & Templates
- Reports are generated using templates in `src/templates/`.
- **Japanese Badge:** Cards with `/jp/` in their URL must display an "Unreleased (JP)" badge in reports.
- **Hover Previews:** Handled via JavaScript in the templates to provide dynamic positioning.

## Automation
A GitHub Action (`.github/workflows/scrape-generate-reports.yaml`) runs the scrape and analysis cycle every 6 hours.
