# "The Blueprint Exists. So Why Is America Still Bleeding?"
### A Data-Driven Magazine Story — Story Skeleton & Flow

---

## Central Question
> **Australia fixed its gun violence problem in one year. NYC has some of the strictest gun laws in America. It's been 30 years. What's going wrong?**

---

## Target Audience
General readers — curious, not necessarily politically aligned. Interested in data and evidence, not preached at. The story lets the data make the argument.

---

## Narrative Genre (Segel & Heer)
**Martini Glass** — guided narrative first, then opens into interactive exploration at the end.

---

## Section 1 — The Benchmark: Australia
**Hook. Set the standard the rest of the story is measured against.**

### Narrative
- 1996, Port Arthur, Tasmania. 35 people killed in a single mass shooting.
- 12 days later, the Australian government passed sweeping national gun reform.
- 650,000 weapons bought back and destroyed.
- Mass shootings essentially stopped.

### Visualization
- Annotated time series: Australian gun deaths before and after 1996
- Clean before/after contrast — this is the "proof it can work" visual

### Key Message
*This is the blueprint. It exists. It worked.*

---

## Section 2 — The Problem: America
**Establish the scale and persistence of the American crisis.**

### Narrative
- Show the national US gun death trend from ~1996 to present
- Annotate major mass shootings (Columbine 1999, Sandy Hook 2012, Las Vegas 2017, Uvalde 2022)
- The contrast with Australia is immediate and stark
- Unlike Australia, the trend does not bend after any single event

### Visualization
- US gun death time series with mass shooting markers
- Side-by-side or overlaid comparison with Australia trend

### Key Message
*The problem hasn't been solved — and it's not for lack of tragedy.*

---

## Section 3 — Has America Tried? Gun Law Timeline
**Audit the policy attempts. Let the data answer honestly.**

### Narrative
Walk through major federal and state gun law moments:
- **1994** — Federal Assault Weapons Ban signed
- **2004** — Federal Assault Weapons Ban expires, not renewed
- **2013** — NY SAFE Act (post-Sandy Hook, one of strictest state laws in US)
- **2022** — *Bruen* Supreme Court ruling loosens NY concealed carry restrictions
- **2022** — Federal Bipartisan Safer Communities Act
- **2023** — NY Concealed Carry Improvement Act (response to Bruen)

### Visualization
- US shooting time series with legislation as annotated vertical lines
- Honest finding: no single law visibly bends the national curve

### Key Message
*America has tried. But the results don't look like Australia.*

---

## Section 4 — The Case Study: New York City
**Zoom in. If anywhere in America should work, it's NYC.**

### Narrative
- NY has the strictest gun laws in the country
- NYC shootings did fall dramatically — from ~2,000/year in 2006 to under 800 by 2019
- That's real progress. But then 2020 happened.
- Even during the good years, the problem never went away entirely
- And not everyone in NYC experienced the improvement equally

### Visualizations
- NYC shooting time series 2006–present, annotated with NY gun law changes
- Interactive map: shooting density by neighborhood over time (use lat/lon data)
- Borough breakdown: which areas improved, which didn't
- Demographic breakdown: who bears the cost (victims by age, race, borough)

### Key Message
*NYC made genuine progress — but couldn't finish the job. Why?*

---

## Section 5 — The Core Tension: Why NYC Isn't Australia
**The analytical heart of the story.**

### Narrative
- Australia worked because it was a **national, sovereign solution**
- NYC can pass strict laws, but it shares a country with states that have almost no restrictions
- The "Iron Pipeline": guns flow into NYC from Virginia, Georgia, Pennsylvania, South Carolina
- Estimated 90%+ of guns used in NYC crimes come from out of state
- Show the contrast: NY gun law strictness vs. neighboring states

### Visualizations
- Flow map: origin states of guns recovered at NYC crime scenes
- Choropleth: US states ranked by gun law strictness vs. firearm death rate
- Scatter plot: gun law strictness score vs. shooting rate, state by state

### Key Message
*NYC is trying to hold back the tide with a bucket. The hole is at the federal level.*

---

## Section 6 — Income & Education (Supporting Layer)
**Why some neighborhoods never recovered even when city-wide numbers improved.**

### Narrative
- Shooting concentration in NYC follows inequality almost exactly
- Low-income, lower-education neighborhoods in the Bronx and Brooklyn bear disproportionate burden
- Neighborhoods that gentrified saw shooting rates fall — but did policy do that, or economics?
- The 2020 surge hit hardest in the same neighborhoods that never fully recovered from the 2008 financial crisis

### Visualizations
- Map overlay: shooting density vs. median household income by ZIP
- Scatter plot: % below poverty line vs. shooting rate per ZIP
- Optional: change over time — neighborhoods that improved economically vs. those that didn't

### Key Message
*Where gun reform hasn't worked, inequality fills the gap.*

---

## Section 7 — Conclusion: The Blueprint Exists
**Close the loop with Australia. Leave the reader with the tension.**

### Narrative
- Australia didn't just pass a law — it passed a *national* law with political consensus and immediate action
- The US has never had that moment, even after Sandy Hook
- NYC's story is not a failure of ambition — it's a structural impossibility without federal action
- End with the honest data-driven conclusion: state-level reform alone is insufficient

### Visualization
- Return to the opening Australia/US comparison — full circle
- Optional: small multiples of countries that reformed nationally vs. the US

### Key Message
*The blueprint exists. The data is clear. What's missing isn't evidence — it's political will at the federal level.*

---

## Full Visualization Lineup

| Section | Visualization Type | Data Source |
|---|---|---|
| Australia | Annotated time series | Australian Institute of Criminology |
| USA national | Time series + mass shooting markers | CDC WONDER / GVA |
| Law changes | Time series with legislation lines | CDC WONDER + public record |
| NYC time series | Annotated line chart | NYPD Shooting Data |
| NYC map | Interactive choropleth/heatmap | NYPD lat/lon data |
| Demographics | Bar charts / stacked area | NYPD victim data |
| Iron pipeline | Flow/Sankey map | ATF tracing data |
| State comparison | Choropleth + scatter | Giffords Law Center + CDC |
| Income overlay | ZIP-level choropleth | ACS / Census |

---

## Data Sources

| Dataset | Source | URL |
|---|---|---|
| NYPD Shooting Incident Data | NYC Open Data | data.cityofnewyork.us |
| US Gun Deaths | CDC WONDER | wonder.cdc.gov |
| Gun Violence Archive | GVA | gunviolencearchive.org |
| Australia gun deaths | AIC / AIHW | aic.gov.au |
| State gun law rankings | Giffords Law Center | giffords.org/lawcenter |
| Iron Pipeline / ATF tracing | ATF | atf.gov |
| NYC Income / Education | ACS via Kaggle or data.census.gov | kaggle.com / data.census.gov |
| NYC Shapefiles | NYC Open Data | data.cityofnewyork.us |

---

## Open Questions / Things to Verify
- [ ] Does the NYPD data include out-of-state gun origin info, or do we need ATF data for that?
- [ ] Is Australian gun death data granular enough for a clean time series?
- [ ] Does the 2006–2019 NYC decline correlate with any specific policy or is it broader NYPD strategy (Stop & Frisk era ends 2013)?
- [ ] How do we handle the 2020 surge narrative — COVID, BLM protests, police pullback? Be careful not to oversimplify.
- [ ] Segel & Heer genre justification needed for Assignment A

---

*Last updated: April 2026*
