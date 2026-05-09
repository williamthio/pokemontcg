# Pokémon TCG Deck Analysis

A Python-based tool for scraping, analyzing, and reporting on Pokémon Trading Card Game (TCG) deck trends from Japanese tournaments listed on [Limitless TCG](https://limitlesstcg.com/tournaments/jp).

## Project Overview

This project automates the collection of competitive tournament data and generates detailed reports on deck archetypes. By calculating card distribution frequencies, it helps players identify standard "skeleton" lists and common tech choices within the meta.

### Key Features
- **Automated Scraping:** Periodically fetches new tournament data and decklists.
- **Archetype Analysis:** Groups decks by their main and secondary Pokémon.
- **Distribution Reports:** Calculates the percentage frequency of card counts (e.g., how often a deck runs 1, 2, or 3 copies of a specific card).
- **Static Site Generation:** Outputs a clean, searchable HTML dashboard using Jinja2 and Semantic UI.

## Tech Stack
- **Python 3.12+**
- **[uv](https://github.com/astral-sh/uv)** for environment management.
- **Scraping:** Requests, BeautifulSoup4, Tenacity.
- **Analysis & Reporting:** Jinja2, Semantic UI.
- **CI/CD:** GitHub Actions for automated 6-hourly updates.

## Getting Started

### Installation
Ensure you have `uv` installed, then clone the repository and sync dependencies:
```bash
uv sync
```

### Usage

#### Scrape Latest Data
To fetch the latest tournament results and append them to the local dataset:
```bash
uv run src/scrape.py
```

#### Generate Reports
To analyze the current dataset and update the HTML reports in the `docs/` folder:
```bash
uv run src/analyze.py
```

## Project Structure
- `src/scrape.py`: Scraper logic for Limitless TCG.
- `src/analyze.py`: Data processing and HTML generation.
- `src/data/`: CSV datasets and scraping progress tracking.
- `src/templates/`: Jinja2 templates for reports.
- `docs/`: The generated static website (viewable via GitHub Pages).

## Automation
The project includes a GitHub Action (`.github/workflows/scrape-generate-reports.yaml`) that automatically runs the scrape and analysis cycle every 6 hours, keeping the reports synchronized with the latest Japanese tournament results.