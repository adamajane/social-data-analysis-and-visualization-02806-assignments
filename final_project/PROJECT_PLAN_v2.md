# 🔫 "How New York Almost Solved Gun Violence" — Project Plan
### A Scrollytelling Deep Dive into NYC Shooting Data (2006–Present)

---

## Central Question

> **NYC shootings are at an all-time low. How did the city get here — and who still bears the cost?**

---

## Narrative Genre

**Martini Glass** (Segel & Heer) — guided narrative through five chapters, opening into free interactive exploration at the end. The "stem" walks the reader through the full data story. The "bowl" hands them the controls to explore themselves.

---

## Data Sources

### Primary — Already cleaned and merged

**`nypd_shootings_combined.csv`** — 24,129 rows — the main analysis file
The three original NYPD datasets (Historic Incidents, YTD Incidents, Victims, Offenders) have been merged and cleaned. One row per incident, with victim and offender fields denormalized in.

| Column | Description |
|--------|-------------|
| `INCIDENT_KEY` | Unique incident identifier |
| `OCCUR_DATE`, `OCCUR_TIME`, `datetime` | Date and time fields |
| `year`, `month`, `day_of_week`, `hour` | Pre-extracted time features |
| `BORO` | Borough (BRONX, BROOKLYN, MANHATTAN, QUEENS, STATEN ISLAND) |
| `PRECINCT` | NYPD precinct number |
| `LOC_OF_OCCUR_DESC` | Inside / Outside |
| `LOC_CLASSFCTN_DESC` | Location type (housing, street, etc.) |
| `Latitude`, `Longitude` | Coordinates for mapping |
| `num_victims` | Number of victims per incident |
| `num_murdered` | Number of fatalities per incident |
| `has_fatality` | Boolean — at least one victim killed |
| `victim_age_groups` | Pipe-separated victim age groups |
| `victim_sexes` | Pipe-separated victim sexes |
| `victim_races` | Pipe-separated victim races |
| `num_offenders` | Number of identified offenders |
| `has_offender_data` | Boolean — offender data available |
| `perp_age_groups` | Pipe-separated offender age groups |
| `perp_sexes` | Pipe-separated offender sexes |
| `perp_races` | Pipe-separated offender races |

**`nypd_victims_clean.csv`** — 28,914 rows — one row per victim
Used for detailed demographic analysis in Chapter 3.

| Column | Description |
|--------|-------------|
| `INCIDENT_KEY` | Join key back to incidents |
| `VICTIM_ID` | Unique victim identifier |
| `VICTIM_AGE_GROUP` | Age group (<18, 18-24, 25-44, 45-64, 65+, UNKNOWN) |
| `VICTIM_SEX` | MALE / FEMALE / UNKNOWN |
| `VICTIM_RACE` | Race/ethnicity |
| `STAT_MURDER_FLG` | Y/N — was this victim killed |
| `is_murder` | Boolean version of above |

**`nypd_offenders_clean.csv`** — 18,903 rows — one row per offender
Used for offender demographics. Note: many incidents have no identified offender.

| Column | Description |
|--------|-------------|
| `INCIDENT_KEY` | Join key back to incidents |
| `PERP_ID` | Unique offender identifier |
| `PERP_AGE_GROUP` | Age group |
| `PERP_SEX` | MALE / FEMALE / UNKNOWN |
| `PERP_RACE` | Race/ethnicity |

### Supplementary — Still needed
| Dataset | Purpose | Source |
|---------|---------|--------|
| NYC Borough Populations by year | Rate per 100k normalization in Chapter 1 | US Census / ACS |

---

## Opening Hook

**"Shootings in New York City are at an all-time low."**

Open with that single sentence. Let it land. Then immediately complicate it:
- *How did we get here?*
- *Did everyone benefit equally?*
- *And what does 20 years of data actually tell us about who gun violence happens to?*

This sets up the whole story — optimistic headline, honest nuance underneath.

---

## Chapter Structure

---

### 📈 Chapter 1 — The Long Decline
**Purpose:** Establish the full arc of the data. Show the reader the shape of the story before zooming in.

#### Narrative
- NYC had roughly 2,000 shooting incidents per year in 2006
- A long, sustained decline brought that number to 777 by 2019 — a roughly 60% reduction over 13 years
- 2020: shootings nearly doubled in a single year — the most dramatic reversal in the dataset
- Since then, a recovery back down to today's all-time low
- Key question for this chapter: was the decline uniform across the city, or did some places improve more than others?

#### Visualizations

Both views below are **one continuous Chapter 1 scrolly**: the same sticky panel first shows the borough multi-line chart (steps 1–5), then swaps to the annotated citywide trend (steps 6–10).

**Viz 1 — NYC Total + Borough Lines (NEW)**
A multi-line chart showing:
- One bold line for NYC as a whole (2006–present)
- Five lighter lines, one per borough (Bronx, Brooklyn, Manhattan, Queens, Staten Island)
- Scroll steps:
  1. Draw in the NYC total line — let the arc land first
  2. Fade in the five borough lines
  3. Highlight the 2006→2019 decline — which boroughs drove it?
  4. Highlight 2020 — did the surge hit all boroughs equally?
  5. Bring it to today — which boroughs are at their own all-time lows?
- Toggle between raw counts and rate per 100k (needed because borough populations differ significantly)

**Viz 2 — NYC Yearly Trend with Legislation Markers (KEEP FROM EXISTING CODE)**
The existing D3 annotated line chart is well-built — keep it. It shows:
- NYC total shootings per year with scroll-triggered steps
- 2020 spike highlighted in red
- Legislation overlay markers as vertical dashed lines
- Fatality rate as a second line on a right-side axis (step 5)

#### Data Work Required
- [ ] Aggregate incidents by year and borough from NYPD data
- [ ] Pull borough population data from ACS for rate normalization
- [ ] Build `borough_yearly.csv` with columns: `year, borough, incidents, population, rate_per_100k`

---

### 🗺️ Chapter 2 — Where It Happens
**Purpose:** The geographic story. Show that the all-time low is a city-wide number — but the burden has never been shared equally.

#### Narrative
- A handful of neighborhoods account for a disproportionate share of all shootings
- Brooklyn and the Bronx consistently dominate — roughly 69% of all incidents
- Even at today's record low, three precincts — 75 (East New York), 73 (Brownsville), 67 (East Flatbush) — stand out
- The decline happened everywhere, but some neighborhoods are still carrying far more than their share

#### Visualizations

**Viz 1 — Heatmap (KEEP FROM EXISTING CODE)**
The existing Leaflet heatmap is well-built — keep all 5 scroll steps:
- Step 1: All shootings 2006–2024
- Step 2: Brooklyn + Bronx (69% of all incidents)
- Step 3: Zoom to precincts 75, 73, 67
- Step 4: 2019 — the floor (777 incidents)
- Step 5: 2020 — the surge (1,532 incidents)

Color gradient: yellow → orange → deep red. CartoDB light base tiles.

#### Data Work Required
- [ ] Confirm lat/lon completeness in cleaned incidents CSV — handle nulls
- [ ] Verify precinct numbers match expected neighborhoods

---

### 👤 Chapter 3 — Who It Happens To
**Purpose:** A demographic portrait of victims. Even at record lows, who bears the cost is remarkably consistent.

#### Narrative
- Victims skew overwhelmingly young and male
- The 18–24 and 25–44 age groups account for the large majority of victims
- Demographic patterns have remained stable across the full 20-year period — the numbers fell, but the profile didn't change
- Note: perpetrator data has high unknown rates — present this honestly with "UNKNOWN" prominently shown

#### Visualizations

**Viz 1 — Demographics Bar Charts (KEEP FROM EXISTING CODE)**
The existing D3 demographics section is well-built — keep it:
- Victim breakdown by age group
- Victim breakdown by sex
- Fatality rates by age group overlaid

**Viz 2 — Demographics Over Time (NEW — optional)**
A stacked area or small multiples showing whether the demographic profile of victims has shifted over the 20-year period. Has the age distribution changed? Has anything moved?

#### Data Work Required
- [ ] `nypd_victims_clean.csv` is already clean — use directly for age/sex breakdowns
- [ ] Quantify UNKNOWN rates in `perp_age_groups` from combined file — show prominently in viz
- [ ] If adding Viz 2: aggregate `nypd_victims_clean.csv` by `year` + `VICTIM_AGE_GROUP`

---

### 🕐 Chapter 4 — When It Happens
**Purpose:** Temporal patterns — time of day, day of week, seasonality. Has the *when* changed even as the numbers fell?

#### Narrative
- Shootings concentrate heavily in late night and early morning hours
- Friday and Saturday nights are the peak — especially the window from 10pm to 4am
- Summer spikes are consistent across all years in the dataset
- The temporal pattern has remained stable across 20 years even as totals declined

#### Visualizations

**Viz 1 — Day × Hour Heatmap (KEEP FROM EXISTING CODE)**
The existing D3 day-of-week × hour-of-day grid is well-built — keep both scroll steps:
- Step 1: Full heatmap — all cells visible
- Step 2: Dims everything except late Friday/Saturday/early Sunday — the peak window

**Viz 2 — Seasonality Chart (NEW — optional)**
A chart showing average shootings by month across all years — the summer spike is a strong visual. Could be a simple bar chart or a radial/circular chart for visual interest.

#### Data Work Required
- [ ] `hour` and `day_of_week` already extracted in `nypd_shootings_combined.csv` — use directly
- [ ] Aggregate by `day_of_week` × `hour` for the heatmap
- [ ] If adding seasonality: aggregate by `month` across all years

---

### ☠️ Chapter 5 — Fatal vs. Non-Fatal
**Purpose:** Lethality. The headline number is shooting incidents — but what share are fatal? Has that changed over time?

#### Narrative
- Not all shootings are murders — the `STATISTICAL_MURDER_FLAG` separates fatal from non-fatal
- Has the fatality rate (% of shootings that are fatal) changed as overall numbers fell?
- A falling number of shootings with a rising lethality rate would tell a very different story
- Are some boroughs or time periods more lethal than others?
- This is a less obvious angle that rewards close reading of the data

#### Visualizations

**Viz 1 — Fatal vs. Non-Fatal Over Time**
A stacked bar or area chart showing fatal and non-fatal incidents per year, with fatality rate as an overlaid line. This is partially built in the existing trend chart (step 5 adds the fatality rate line) — expand on it here as a dedicated section.

**Viz 2 — Lethality by Borough**
Small multiples or grouped bars showing fatality rate per borough. Are some boroughs more lethal per shooting than others?

#### Data Work Required
- [ ] Use `has_fatality` and `num_murdered` from `nypd_shootings_combined.csv`
- [ ] Compute fatal and non-fatal counts per year and per `BORO`
- [ ] Compute fatality rate: `num_murdered / num_victims` per year

---

### 🔍 Exploration — Open the Martini Glass
**Purpose:** Hand the reader the controls. Let them find their own story.

#### Description
**(KEEP FROM EXISTING CODE — fully built)**

The existing interactive exploration section is complete and well-built:
- Borough dropdown filter
- Dual year range sliders
- Age group toggle buttons
- Sex toggle buttons
- Live stats readout: incidents, victims, fatalities, fatality rate
- Leaflet heatmap that updates in real time

This is the "bowl" of the Martini Glass — everything before this was the guided stem.

---

## Full Visualization Lineup

| Chapter | Visualization | Status |
|---------|--------------|--------|
| 1 | NYC total + borough multi-line chart | **NEW — build** |
| 1 | Annotated trend line with legislation markers | **KEEP existing** |
| 2 | Leaflet heatmap with 5 scroll steps | **KEEP existing** |
| 3 | Demographics bar charts (age, sex) | **KEEP existing** |
| 3 | Demographics over time (optional) | **NEW — optional** |
| 4 | Day × hour heatmap grid | **KEEP existing** |
| 4 | Seasonality by month (optional) | **NEW — optional** |
| 5 | Fatal vs. non-fatal stacked chart | **NEW — build** |
| 5 | Lethality by borough | **NEW — build** |
| End | Interactive exploration (full filters) | **KEEP existing** |

---

## Data Cleaning Checklist

### Already done (in merged files)
- [x] Parse `OCCUR_DATE` and `OCCUR_TIME` into proper datetime
- [x] Extract `year`, `month`, `day_of_week`, `hour`
- [x] Fix dirty age group values → `UNKNOWN`
- [x] Standardize borough names
- [x] `STAT_MURDER_FLG` converted to boolean `is_murder`
- [x] Join incidents → victims on `INCIDENT_KEY`
- [x] Join incidents → offenders on `INCIDENT_KEY`
- [x] Victim/offender fields denormalized into incidents file

### Still needed
- [ ] Verify lat/lon null rate in `nypd_shootings_combined.csv` — confirm coverage for mapping
- [ ] Quantify UNKNOWN rates in `perp_age_groups`, `perp_sexes`, `perp_races` — report honestly in Chapter 3
- [ ] Pull NYC borough population by year from ACS for rate normalization
- [ ] Build `borough_yearly.csv`: aggregate by `year` and `BORO`, join population, compute `rate_per_100k`
- [ ] Verify `has_offender_data` — what % of incidents have no offender identified?

---

## Segel & Heer Genre Justification

**Genre: Martini Glass**

The story has a clear guided narrative (Chapters 1–5) that needs to be experienced in sequence for the argument to build properly. But the NYC data is rich enough to reward open exploration. The Martini Glass lets us do both — walk the reader through the evidence, then hand them the controls.

**Visual narrative tools used:**
- *Ordering:* Linear author-driven path through 5 chapters
- *Highlighting:* Scroll-triggered annotation reveals, color emphasis on key moments (2020 spike in red, decline in gold)
- *Interactivity:* Concentrated in the final exploration section and within-chart tooltips
- *Messaging:* Section headers, step captions, chart annotations, inline statistics

---

## Open Questions

- [ ] Do we want per-capita (rate per 100k) or raw counts as the primary metric? Recommend offering a toggle in Chapter 1
- [ ] How do we handle the YTD 2024/2025 data — include as partial year or exclude?
- [ ] Perpetrator data — include with heavy caveats about unknown rates, or drop entirely?
- [ ] Do we want a written conclusion section after the exploration, or let the data speak for itself?

---

*Last updated: May 2026*
