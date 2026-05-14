# Pokémon TCG Deck Analysis

Python tool for scraping and analyzing Japanese tournament trends from Limitless TCG.

## Core Stack
- **Engine:** Python 3.12+ | [uv](https://github.com/astral-sh/uv)
- **UI:** Tailwind CSS (Modern Dashboard), Jinja2 Templates
- **Data:** BeautifulSoup4 (Scraping), Tenacity (Retries)
- **Verification:** Playwright (Chromium)

## Project Structure
- `src/scrape.py`: Scrapes tournament/deck data to `src/data/tournament_decks.csv`.
- `src/analyze.py`: Processes CSV and generates HTML reports in `docs/`.
- `src/templates/`: Jinja2 source files (`base.html`, `index.html`, `cluster_report.html`).
- `docs/`: Deployment target for the static analytics site.

## Key Workflows

### 1. Data Update & Generation
```bash
uv run src/scrape.py    # Append new tournament data
uv run src/analyze.py   # Regenerate all HTML reports
```

### 2. UI Verification
Always verify UI changes (especially hover previews and navigation) using **Playwright Chromium**. 
- **Method:** Serve `docs/` locally or navigate via `file://` protocols.
- **Critical Checks:**
    - Archetype names on `index.html` link to full reports.
    - Card hover previews are viewport-relative (no clipping) and 320px wide.
    - Image fallback: Primary (DigitalOcean) -> Fallback (Limitless Proxy).
    - Card numbers must be 3-digit zero-padded (`zfill(3)`) for asset matching.

## UI Conventions
- **Theming:** Dark mode glassmorphism via Tailwind.
- **Image Pattern:** `.../tpci/[SET]/[SET]_[NUM]_R_EN.png` (NUM must be padded).
- **Positioning:** Hover previews use JS-based dynamic positioning to avoid `overflow-hidden` constraints.
