"""
NYPD Shooting Data — Cleaning, Preprocessing & Combination
===========================================================
Course: Social Data Analysis and Visualization (DTU)
Project: "The Blueprint Exists" — Act 3 (NYC Deep Dive)

Input files (from NYC Open Data, downloaded 2026-05-02):
  - Shootings__2006-Present__20260502.csv      (24,127 incidents)
  - Shooting_Victims__2006-Present__20260502.csv (28,912 victims)
  - Shooting_Offenders__2006-Present__20260502.csv (18,901 offenders)

Output files:
  - nypd_shootings_combined.csv  (incident-level, all three tables joined)
  - nypd_victims_clean.csv       (victim-level detail)
  - nypd_offenders_clean.csv     (offender-level detail)
"""

import pandas as pd
from pathlib import Path

# ============================================================
# Configuration — adjust these paths as needed
# ============================================================

RAW_DIR = Path("data/raw")
OUT_DIR = Path("data/clean")
OUT_DIR.mkdir(parents=True, exist_ok=True)

SHOOTINGS_FILE = RAW_DIR / "Shootings__2006-Present__20260502.csv"
VICTIMS_FILE   = RAW_DIR / "Shooting_Victims__2006-Present__20260502.csv"
OFFENDERS_FILE = RAW_DIR / "Shooting_Offenders__2006-Present__20260502.csv"

VALID_AGE_GROUPS = ["<18", "18-24", "25-44", "45-64", "65+", "UNKNOWN"]


# ============================================================
# 1. Load raw data
# ============================================================

shootings = pd.read_csv(SHOOTINGS_FILE)
victims   = pd.read_csv(VICTIMS_FILE)
offenders = pd.read_csv(OFFENDERS_FILE)

print("=== Raw data loaded ===")
print(f"  Shootings:  {shootings.shape[0]:,} rows × {shootings.shape[1]} cols")
print(f"  Victims:    {victims.shape[0]:,} rows × {victims.shape[1]} cols")
print(f"  Offenders:  {offenders.shape[0]:,} rows × {offenders.shape[1]} cols")


# ============================================================
# 2. Clean Shootings table
# ============================================================

# 2a. Fix lat/lon swap
#     The source CSV has the columns mislabeled:
#       "Latitude" column contains longitude values (~-73.7 to -74.2)
#       "Longitude" column contains latitude values (~40.5 to 40.9)
shootings = shootings.rename(columns={
    "Latitude":  "Longitude_raw",
    "Longitude": "Latitude_raw",
})
shootings = shootings.rename(columns={
    "Longitude_raw": "Longitude",
    "Latitude_raw":  "Latitude",
})

# Sanity check: NYC lat should be ~40.5–40.9, lon ~-74.3 to -73.7
assert shootings["Latitude"].dropna().between(40.4, 41.0).all(), \
    "Latitude values out of expected NYC range after swap"
assert shootings["Longitude"].dropna().between(-74.3, -73.6).all(), \
    "Longitude values out of expected NYC range after swap"

# 2b. Parse datetime and extract temporal features
shootings["datetime"] = pd.to_datetime(
    shootings["OCCUR_DATE"] + " " + shootings["OCCUR_TIME"],
    format="%m/%d/%Y %H:%M:%S",
)
shootings["year"]        = shootings["datetime"].dt.year
shootings["month"]       = shootings["datetime"].dt.month
shootings["day_of_week"] = shootings["datetime"].dt.day_name()
shootings["hour"]        = shootings["datetime"].dt.hour

# 2c. Fill missing jurisdiction codes
#     2 rows have NaN — fill with -1 to indicate "unknown"
shootings["JURISDICTION_CODE"] = (
    shootings["JURISDICTION_CODE"].fillna(-1).astype(int)
)

print(f"\n=== Shootings cleaned ===")
print(f"  Lat/lon swap corrected")
print(f"  Datetime parsed, temporal features extracted")
print(f"  Null counts:\n{shootings.isnull().sum().to_string()}")


# ============================================================
# 3. Clean Victims table
# ============================================================

# 3a. Fix dirty age values
#     Found 1 invalid entry: "1022" — likely a data entry error
dirty_victim_ages = victims[~victims["VICTIM_AGE_GROUP"].isin(VALID_AGE_GROUPS)]
if len(dirty_victim_ages) > 0:
    print(f"\n=== Dirty victim age values (→ UNKNOWN) ===")
    print(f"  {dirty_victim_ages['VICTIM_AGE_GROUP'].value_counts().to_dict()}")
    victims.loc[
        ~victims["VICTIM_AGE_GROUP"].isin(VALID_AGE_GROUPS),
        "VICTIM_AGE_GROUP",
    ] = "UNKNOWN"

# 3b. Fill NaN in string demographic columns
for col in ["VICTIM_AGE_GROUP", "VICTIM_SEX", "VICTIM_RACE"]:
    victims[col] = victims[col].fillna("UNKNOWN")

# 3c. Create boolean murder flag
victims["is_murder"] = victims["STAT_MURDER_FLG"] == "Y"

print(f"\n=== Victims cleaned: {victims.shape[0]:,} rows ===")


# ============================================================
# 4. Clean Offenders table
# ============================================================

# 4a. Fix dirty age values
#     Found 6 invalid entries: 1020, 1028, 2021, 940, 224, 1822
dirty_perp_ages = offenders[~offenders["PERP_AGE_GROUP"].isin(VALID_AGE_GROUPS)]
if len(dirty_perp_ages) > 0:
    print(f"\n=== Dirty perp age values (→ UNKNOWN) ===")
    print(f"  {dirty_perp_ages['PERP_AGE_GROUP'].value_counts().to_dict()}")
    offenders.loc[
        ~offenders["PERP_AGE_GROUP"].isin(VALID_AGE_GROUPS),
        "PERP_AGE_GROUP",
    ] = "UNKNOWN"

# 4b. Fill NaN in string demographic columns
for col in ["PERP_AGE_GROUP", "PERP_SEX", "PERP_RACE"]:
    offenders[col] = offenders[col].fillna("UNKNOWN")

print(f"\n=== Offenders cleaned: {offenders.shape[0]:,} rows ===")


# ============================================================
# 5. Combine into incident-level master table
# ============================================================

# 5a. Aggregate victim info per incident
vic_agg = (
    victims.groupby("INCIDENT_KEY")
    .agg(
        num_victims=("VICTIM_ID", "count"),
        num_murdered=("is_murder", "sum"),
        victim_age_groups=("VICTIM_AGE_GROUP", lambda x: "|".join(x.astype(str))),
        victim_sexes=("VICTIM_SEX", lambda x: "|".join(x.astype(str))),
        victim_races=("VICTIM_RACE", lambda x: "|".join(x.astype(str))),
    )
    .reset_index()
)
vic_agg["num_murdered"] = vic_agg["num_murdered"].astype(int)
vic_agg["has_fatality"] = vic_agg["num_murdered"] > 0

# 5b. Aggregate offender info per incident
off_agg = (
    offenders.groupby("INCIDENT_KEY")
    .agg(
        num_offenders=("PERP_ID", "count"),
        perp_age_groups=("PERP_AGE_GROUP", lambda x: "|".join(x.astype(str))),
        perp_sexes=("PERP_SEX", lambda x: "|".join(x.astype(str))),
        perp_races=("PERP_RACE", lambda x: "|".join(x.astype(str))),
    )
    .reset_index()
)

# 5c. Left join: shootings ← victims ← offenders
#     Left join ensures every incident is kept even if victim/offender
#     records are missing (2 victim keys and 1 offender key are orphans
#     in the raw data — they get dropped by the left join on shootings)
combined = shootings.merge(vic_agg, on="INCIDENT_KEY", how="left")
combined = combined.merge(off_agg, on="INCIDENT_KEY", how="left")

# 5d. Mark offender data availability
combined["has_offender_data"] = combined["num_offenders"].notna()
combined["num_offenders"] = combined["num_offenders"].fillna(0).astype(int)


# ============================================================
# 6. Summary statistics
# ============================================================

print("\n" + "=" * 60)
print("COMBINED DATASET SUMMARY")
print("=" * 60)
print(f"Shape: {combined.shape[0]:,} rows × {combined.shape[1]} cols")
print(f"Year range: {combined['year'].min()} – {combined['year'].max()}")
print(f"Latitude range:  {combined['Latitude'].min():.4f} – {combined['Latitude'].max():.4f}")
print(f"Longitude range: {combined['Longitude'].min():.4f} – {combined['Longitude'].max():.4f}")
print(f"Total victims across all incidents: {combined['num_victims'].sum():,}")
print(f"Total fatalities: {combined['num_murdered'].sum():,}")
print(f"Incidents with fatalities: {combined['has_fatality'].sum():,} "
      f"({100 * combined['has_fatality'].mean():.1f}%)")
print(f"Incidents with offender data: {combined['has_offender_data'].sum():,} "
      f"({100 * combined['has_offender_data'].mean():.1f}%)")
print(f"Incidents with NO offender data: "
      f"{(~combined['has_offender_data']).sum():,} "
      f"({100 * (~combined['has_offender_data']).mean():.1f}%)")

print(f"\nPartial years:")
for y in [2025, 2026]:
    n = (combined["year"] == y).sum()
    max_month = combined.loc[combined["year"] == y, "month"].max()
    print(f"  {y}: {n} incidents (data through month {max_month})")

print(f"\nIncidents per year (2006–2024):")
yearly = combined[combined["year"] <= 2024].groupby("year").size()
print(yearly.to_string())


# ============================================================
# 7. Save cleaned files
# ============================================================

combined.to_csv(OUT_DIR / "nypd_shootings_combined.csv", index=False)
victims.to_csv(OUT_DIR / "nypd_victims_clean.csv", index=False)
offenders.to_csv(OUT_DIR / "nypd_offenders_clean.csv", index=False)

print(f"\n=== Files saved to {OUT_DIR}/ ===")
print(f"  nypd_shootings_combined.csv  ({combined.shape[0]:,} rows)")
print(f"  nypd_victims_clean.csv       ({victims.shape[0]:,} rows)")
print(f"  nypd_offenders_clean.csv     ({offenders.shape[0]:,} rows)")
