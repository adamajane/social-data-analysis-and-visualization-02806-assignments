# Generated web bundle

- Run **`build_visuals.ipynb`** (first code cell) with working directory **`final_project/`**.
- Output: **`dashboard_data.json`** — incidents, aggregates, victims, and offender summaries for `index_plan_v2.html`.
- Optional PNGs: **`figures/*.png`** after running the matplotlib cells in the notebook.

If `dashboard_data.json` is present, the page loads it and skips parsing the large CSVs in the browser (faster). Delete this file to force the CSV pipeline.

The JSON is large (~13 MB); you may add `generated/dashboard_data.json` to `.gitignore` and regenerate locally.
