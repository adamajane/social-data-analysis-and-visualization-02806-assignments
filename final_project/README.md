# Final Project — NYC Gun Violence

Final project for DTU **Social Data Analysis and Visualization (02806)**. We analyze two decades of NYPD shooting incidents (2006–2026) and present the findings two ways:

- **[`index.html`](index.html)** — the public-facing data story (martini-glass narrative, interactive map explorer at the end).
- **[`explainer_notebook.ipynb`](explainer_notebook.ipynb)** — the technical companion notebook covering motivation, cleaning, EDA, findings, genre/narrative choices, and discussion.

## Project structure

```
final_project/
├── index.html                  # Public data story
├── explainer_notebook.ipynb    # Technical explainer (run this)
├── data/
│   ├── raw/                    # Original NYC Open Data CSVs (incidents, victims, offenders)
│   ├── clean/                  # Cleaned/typed versions written by the notebook
│   ├── nypd_shootings_combined.csv
│   ├── nypd_victims_clean.csv
│   ├── nypd_offenders_clean.csv
│   ├── nyc_police_precincts.geojson   # Precinct boundaries for choropleths
│   └── legislation_events.json        # Annotated policy/legislation timeline
├── generated/
│   ├── dashboard_data.json     # Aggregates consumed by index.html
│   └── figures/                # Static PNGs used in the explainer / story
└── output/
    ├── chapter2_leaflet_symbol_map.html
    └── nyc_shootings_precinct_map_explorer.html  # Embedded into index.html
```

## Data

All shooting data comes from **[NYC Open Data — NYPD Shooting Incident Data (Historic + Year-To-Date)](https://opendata.cityofnewyork.us/)**. The three raw exports in `data/raw/` cover incidents, victims, and offenders (2006–2026). Precinct geometry is the city's published precinct GeoJSON; the legislation timeline is hand-curated from public sources cited in the notebook.

## Running the notebook

The repository uses [**uv**](https://docs.astral.sh/uv/) for dependency management. Dependencies (pandas, numpy, matplotlib, plotly, scipy, ipykernel) are declared in the root `pyproject.toml`.

### 1. Install uv

```bash
# macOS and Linux, standalone installer
curl -LsSf https://astral.sh/uv/install.sh | sh

# macOS and Linux, Homebrew
brew install uv

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Sync the environment

From the **repository root** (one level up from `final_project/`):

```bash
uv sync
```

This creates a `.venv/` with Python ≥ 3.14 and all pinned dependencies from `uv.lock`.

### 3. Launch Jupyter

Still from the repository root:

```bash
uv run jupyter notebook final_project/explainer_notebook.ipynb
```

Then **Run All** (Cell → Run All, or `⇧⏎` through each cell). The notebook reads from `data/`, writes cleaned CSVs into `data/clean/`, and refreshes `generated/dashboard_data.json` and `generated/figures/`.

### Alternatives

- **JupyterLab:** `uv run jupyter lab`
- **VS Code:** open the notebook and select the `.venv` interpreter as the kernel.
- **One-off cell execution:** `uv run jupyter nbconvert --to notebook --execute final_project/explainer_notebook.ipynb`

## Viewing the website

`index.html` is fully static — open it directly in a browser, or serve it from the repo root:

```bash
uv run python -m http.server 8000
# then visit http://localhost:8000/final_project/
```

A local server is recommended because the page fetches `generated/dashboard_data.json` and the embedded Leaflet map from `output/`, which some browsers block under the `file://` protocol.
