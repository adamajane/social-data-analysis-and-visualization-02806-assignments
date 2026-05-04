# 🔫 "The Blueprint Exists" — Project Plan
### A Scrollytelling Data Story on Gun Reform: From Australia to NYC

---

## Central Question

> **Australia proved that national gun reform works. New York City — with some of the strictest gun laws in America — is the country's best attempt at the local level. What does nearly 20 years of NYPD shooting data reveal about what local reform can and can't achieve?**

---

## Narrative Genre

**Martini Glass** (Segel & Heer) — guided narrative through three acts, opening into interactive exploration at the end. The "stem" of the glass walks the reader through Australia → US → NYC. The "bowl" at the end lets them explore the NYC data interactively (map, filters, timeline).

---

## Story Structure: Three Acts

### 🌏 Act 1 — "The Proof It Can Work" (Australia)
**Purpose:** Establish the benchmark. Show the reader that gun reform *has* worked — decisively — when implemented at a national level.

#### Sections

**1.1 — Port Arthur & The Response**
- April 1996: 35 killed in a single mass shooting in Tasmania
- Within 12 days: National Firearms Agreement passed
- 650,000+ weapons bought back and destroyed
- Bipartisan political consensus — not a left/right issue in Australia

**1.2 — The Data: Before & After**
- Gun death rate dropped from ~2.9 per 100k (1996) to ~0.88 per 100k (2018)
- 13 mass shootings in the 18 years before reform, essentially zero in the 22 years after
- Chapman et al. (2018) estimated ~16 mass shootings *would have occurred* without intervention

#### Visualizations
| Viz | Type | Data Source |
|-----|------|-------------|
| Australian gun deaths over time (total, homicide, suicide) | Annotated line chart with 1996 marker | gunpolicy.org / ABS |
| Mass shootings timeline: before vs. after | Event timeline or lollipop chart | Published records |

#### Data Work Required
- Manually compile yearly Australian gun death figures from gunpolicy.org (they publish the numbers — data goes back to 1979)
- Small CSV: ~40 rows (year, total_deaths, homicides, suicides, rate_per_100k)
- Effort: **Low** (~1 hour)

---

### 🇺🇸 Act 2 — "The Country That Couldn't" (United States)
**Purpose:** Contrast. Show that the US has had *plenty* of tragedy but has never achieved the national consensus Australia did. Introduce the legislative landscape.

#### Sections

**2.1 — The Scale of the Problem**
- ~48,000 firearm deaths in the US in 2022 (~132 per day)
- Firearms are a leading cause of death for Americans aged 1–44
- The trend does not bend after any single mass shooting event

**2.2 — The Policy Attempts**
Walk the reader through key federal and NY State moments:
- **1994** — Federal Assault Weapons Ban signed
- **2004** — Ban expires, not renewed
- **2013** — NY SAFE Act (post-Sandy Hook, one of strictest state laws)
- **2022** — *Bruen* Supreme Court ruling (loosens NY concealed carry)
- **2022** — Federal Bipartisan Safer Communities Act
- **2023** — NY Concealed Carry Improvement Act (response to *Bruen*)

**2.3 — The Bridge to NYC**
- "If strict gun laws alone could solve this, New York should be the safest place in America. Let's look at what the data actually says."

#### Visualizations
| Viz | Type | Data Source |
|-----|------|-------------|
| US gun deaths over time | Line chart with mass shooting event markers | CDC WONDER / The Trace |
| Australia vs. US rate comparison | Dual-axis or small multiples | gunpolicy.org + CDC |
| US legislative timeline | Annotated vertical lines on trend | Public record |

#### Data Work Required
- Download US firearm mortality data from CDC WONDER or The Trace's pre-cleaned datasets
- Compile a short list of key gun legislation dates with descriptions (federal + NY State)
- Small CSV: ~25 rows for yearly US totals, plus a separate legislation_events.csv
- Effort: **Low–Medium** (~2 hours)

---

### 🗽 Act 3 — "New York's Experiment" (NYC Deep Dive)
**Purpose:** This is the analytical heart. Your NYPD data is the star. Show what local reform achieved, where it fell short, and why.

#### Sections

**3.1 — The Big Picture: NYC Shooting Trends (2006–Present)**
- Shootings declined dramatically: from ~2,000/year (2006) to under 800 by 2019
- That's real, measurable progress — a ~60% reduction over 13 years
- Then 2020: shootings nearly doubled in a single year
- Overlay NY gun law changes on the timeline — do any visibly bend the curve?

**3.2 — Where It Happens: The Geography of Gun Violence**
- Interactive heatmap/choropleth of shootings by location
- Borough breakdown: Bronx and Brooklyn bear disproportionate burden
- Precinct-level analysis: which areas improved, which didn't
- Show concentration — a small number of neighborhoods account for a huge share
- Inside vs. outside breakdown, location types (street, housing, commercial)

**3.3 — Who's Affected: Victims & Perpetrators**
- Age group distributions (victims skew young — heavy in 18-24 and 25-44)
- Sex breakdown (overwhelmingly male on both sides)
- Race/ethnicity patterns (handle with care — present factually, contextualize)
- Murder flag: what percentage of shootings are fatal? Has lethality changed over time?
- **Important caveat:** Perpetrator data has high unknown rates (many cases unsolved)

**3.4 — When It Happens: Temporal Patterns**
- Time of day (likely peaks late night / early morning)
- Day of week (weekends vs. weekdays)
- Seasonal patterns (summer spikes?)
- How COVID disrupted (or amplified) these patterns

**3.5 — The 2020 Question**
- Dedicated section on the surge: what happened?
- Map it: did the surge hit everywhere equally, or concentrate in specific areas?
- Was it a temporary spike or a structural shift? (Look at 2021–present recovery)
- Be honest about competing explanations (COVID stress, policing changes, economic disruption) — acknowledge you can't isolate a single cause

**3.6 — What the Data Can't Tell Us (honest limitations)**
- NYPD data doesn't include where guns originated (need ATF data for Iron Pipeline)
- Correlation ≠ causation: policy overlay shows co-occurrence, not proof
- Perpetrator data is incomplete by nature
- The data captures *reported* shootings — there may be underreporting

#### Visualizations
| Viz | Type | Data Source |
|-----|------|-------------|
| NYC yearly shooting trend | Annotated line chart with legislation markers | NYPD Shootings |
| Interactive shooting map | Heatmap or dot map with time slider | NYPD lat/lon |
| Borough comparison | Small multiples or stacked area chart | NYPD Shootings |
| Victim demographics | Grouped bar charts or population pyramids | NYPD Victims |
| Perpetrator demographics (with caveat) | Bar charts with "unknown" prominently shown | NYPD Offenders |
| Time-of-day / day-of-week | Radial chart or heatmap grid | NYPD Shootings |
| Murder rate over time | Line chart (fatal vs. non-fatal) | NYPD Victims |
| 2020 surge: before/during/after map | Side-by-side or animated maps | NYPD Shootings |

#### Data Work Required
- Download all three NYPD datasets from NYC Open Data
- Join on INCIDENT_KEY (one-to-many: incidents → victims, incidents → offenders)
- Data cleaning checklist:
  - [ ] Parse OCCUR_DATE and OCCUR_TIME into proper datetime
  - [ ] Handle null/missing lat/lon values (some incidents may lack coordinates)
  - [ ] Check for dirty values in age groups (sometimes contains typos like "940" or "224")
  - [ ] Standardize borough names if inconsistent
  - [ ] Flag and quantify "UNKNOWN" rates in perpetrator demographics
  - [ ] Verify STAT_MURDER_FLG values (YES/NO → boolean)
- Feature engineering:
  - [ ] Extract year, month, day_of_week, hour from datetime
  - [ ] Create a "period" column (pre-2013 SAFE Act, post-SAFE Act, COVID era, post-COVID)
  - [ ] Calculate per-borough yearly rates (will need borough population data for normalization)
  - [ ] Compute rolling averages for trend smoothing
- Effort: **Medium–High** (~6-8 hours for cleaning + EDA)

---

## 🔄 Conclusion / Synthesis

Bring it full circle:
- Australia reformed nationally → gun violence dropped
- The US has never achieved national consensus
- NYC went as far as a single city can go — and the data shows real progress
- But local reform has structural limits (can't control gun supply flowing in from other states)
- End with the tension: "The blueprint exists. The evidence is clear. What's missing isn't data — it's political will at the federal level."

**Final interactive element:** Open up the Martini Glass — let the reader explore the NYC data themselves with filters (borough, year range, demographics, time of day).

---

## Data Sources Summary

| Dataset | Source | Format | Effort |
|---------|--------|--------|--------|
| **NYPD Shooting Incidents** | NYC Open Data | CSV (downloadable) | Primary dataset — heavy analysis |
| **NYPD Shooting Victims** | NYC Open Data | CSV (downloadable) | Primary dataset — joins to incidents |
| **NYPD Shooting Offenders** | NYC Open Data | CSV (downloadable) | Primary dataset — joins to incidents |
| Australian gun deaths (yearly) | gunpolicy.org + ABS | Manual transcription → CSV | Light — ~40 rows |
| US gun deaths (yearly) | CDC WONDER or The Trace Data Hub | Downloadable | Light — aggregate national totals |
| Key gun legislation dates | Public record (compiled manually) | Manual → CSV/JSON | Light — ~10-15 events |
| NYC borough populations (for rate normalization) | US Census / ACS | Downloadable | Light — 5 boroughs × ~20 years |

**Total datasets: 4 core + 3 supplementary**
The NYPD triplet is your deep analysis. Everything else is context-setting.

---

## Task Breakdown & Timeline

### Week 1-2 (Before video deadline)
- [ ] Download all three NYPD datasets
- [ ] Download/compile Australia + US aggregate data
- [ ] Compile gun legislation timeline (federal + NY State)
- [ ] Initial data cleaning and EDA on NYPD data
- [ ] Generate key stats for the video: total incidents, year range, borough split, 2020 spike magnitude
- [ ] Create mockup visualizations (can be simple Plotly/matplotlib for the video)
- [ ] Record 1-minute video explaining the concept, central question, genre choice, and preliminary findings

### Week 3-4 (Core analysis)
- [ ] Deep EDA: geographic clustering, temporal patterns, demographic breakdowns
- [ ] Build the legislative timeline overlay on NYC shooting trends
- [ ] Create the interactive map (Leaflet/Folium or Mapbox via Scrollama)
- [ ] Analyze the 2020 surge in detail (spatial + temporal + demographic shifts)
- [ ] Build Australia and US context charts
- [ ] Start writing narrative text for each act

### Week 5+ (Website & polish)
- [ ] Build scrollytelling website (Scrollama + D3/Plotly)
- [ ] Integrate all visualizations into the scroll-driven narrative
- [ ] Write the explainer Jupyter Notebook (motivation, stats, analysis, genre justification, contributions)
- [ ] Test, iterate, polish
- [ ] Peer review within group

---

## Segel & Heer Genre Justification (for Assignment A)

**Genre: Martini Glass**

- **Why:** The story has a clear guided narrative (Australia → US → NYC) that needs to be told in sequence for the argument to land. But the NYC data is rich enough to reward open exploration. The Martini Glass lets us do both — walk the reader through the argument, then hand them the controls.

**Visual Narrative tools (Figure 7):**
- *Visual structuring:* Consistent visual platform (scrollytelling), progress indicators, establishing shot (Australia map/chart opens the story)
- *Highlighting:* Annotations on timeline charts (legislation dates), color-coding for boroughs, feature distinction via interactive filters
- *Transition guidance:* Scroll-triggered transitions between acts, animated chart updates as user scrolls

**Narrative Structure tools (Figure 7):**
- *Ordering:* Linear author-driven path through three acts (user-directed within the final exploration)
- *Interactivity:* Filtering, hovering, time slider on map (concentrated in Act 3 and the open exploration section)
- *Messaging:* Captions, annotations, section headers, introductory text for each act

---

## Open Questions to Resolve

- [ ] Does the NYPD data need borough population normalization? (Probably yes for fair comparisons — source: ACS/Census)
- [ ] How granular is the Australian data? Can we get post-2010 numbers from ABS?
- [ ] For the US national data: use CDC WONDER directly, or The Trace's cleaned version?
- [ ] The 2020 surge — do we frame it as COVID-related, policing-related, or explicitly multi-causal?
- [ ] How much do we want to editorialize vs. let the data speak? (Recommendation: be factual in the body, save the "political will" framing for the conclusion)

---

*Last updated: April 2026*
