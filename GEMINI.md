# Pokémon TCG Deck Analysis

This project is a Python-based tool for scraping, analyzing, and reporting on Pokémon Trading Card Game (TCG) deck trends from Japanese tournaments listed on Limitless TCG.

## Project Overview

The project automates the collection of tournament data and generates detailed cluster analysis reports. It identifies popular deck archetypes and calculates the distribution of cards within those archetypes, providing insights into common card counts and variations.

### Core Technologies
- **Language:** Python 3.12+
- **Dependency Management:** [uv](https://github.com/astral-sh/uv)
- **Scraping:** `requests`, `beautifulsoup4`, `tenacity` (for retries)
- **Reporting:** `Jinja2` (HTML templates), `Semantic UI` (CSS framework)
- **Automation:** GitHub Actions

## Directory Structure

- `src/`: Core source code.
    - `scrape.py`: Scrapes tournament and deck data from Limitless TCG.
    - `analyze.py`: Processes scraped data and generates HTML reports.
    - `data/`: Stores raw and processed data.
        - `tournament_decks.csv`: Main dataset containing scraped decklists.
        - `progress.txt`: Tracks scraped tournament IDs to avoid redundant work.
    - `templates/`: Jinja2 templates for HTML report generation.
- `docs/`: Contains the generated static website (HTML reports).
- `.github/workflows/`: Automation scripts for periodic data updates.

## Building and Running

This project uses `uv` for managing the environment and dependencies.

### Installation
Ensure you have `uv` installed, then run:
```bash
uv sync
```

### Data Scraping
To scrape the latest tournament data:
```bash
uv run src/scrape.py
```
This script identifies new tournaments since the last run and appends them to `src/data/tournament_decks.csv`.

### Analysis and Report Generation
To process the data and update the HTML reports:
```bash
uv run src/analyze.py
```
This will:
1. Clean the `docs/` folder (excluding CSS/JS if present).
2. Analyze the top deck combinations.
3. Generate archetype-specific reports for top 1, 4, 8, and 16 placements.
4. Update `docs/index.html` with the latest summary.

## Development Conventions

- **Data Storage:** Raw deck data is stored in a pipe-separated format within the `cards` column of `tournament_decks.csv`.
- **Archetype Identification:** Decks are grouped by their "Main" and "Secondary" Pokémon as identified on Limitless TCG.
- **Card Distribution:** The analysis calculates the percentage of decks that include a specific card at various counts (e.g., "70% of decks run 4 copies of Battle VIP Pass").
- **Templates:** When modifying report layouts, edit the files in `src/templates/`. The project uses Semantic UI for styling.
- **GitHub Actions:** The `scrape-generate-reports.yaml` workflow runs every 6 hours, automating the scrape and analysis cycles and committing the results back to the repository.
