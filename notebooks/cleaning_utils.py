# cleaning_utils.py
import re
import numpy as np
import pandas as pd


# 1 Parse DateTime, create weekday/weekend and daytime/nighttime
def add_time_variables(df, datetime_col="DateTime"):
    df[datetime_col] = pd.to_datetime(df[datetime_col])

    df["Hour"] = df[datetime_col].dt.hour
    df["Weekday"] = df[datetime_col].dt.day_name()
    df["Weekend"] = df["Weekday"].isin(["Saturday", "Sunday"])
    df["Daytime"] = df["Hour"].between(6, 17)
    df["Time of Day"] = np.where(df["Daytime"], "Daytime", "Nighttime")
    return df


# 2. coerce injury counts, driver age, BAC, and AADT to numeric
def coerce_numeric(df, cols):
    """Convert listed columns to numeric with errors='coerce'."""
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


# 3. To transform `Impact Speed` from range to average value
def impact_speed_to_numeric(series):
    """'11 to 15 MPH' -> 13.0, '35 MPH' -> 35.0, 'Unknown' -> NaN."""

    def _parse(value):
        if pd.isna(value):
            return np.nan
        text = str(value)
        nums = re.findall(r"\d+", text)
        if not nums:
            return np.nan
        nums = [float(n) for n in nums]
        return sum(nums) / len(nums)

    return series.apply(_parse)


# 4. To transform `Number of Vehicles` from string to numeric
def vehicles_to_numeric(series):
    """'2 Vehicles' -> 2."""
    return series.astype(str).str.extract(r"(\d+)", expand=False).astype(float)


# 5. To transform `Speed Limit` stored as text labels (e.g., "35 MPH") to numeric (35.0)
def speed_limit_to_numeric(series):
    """'35 MPH' -> 35."""
    cleaned = series.astype(str).str.replace(" MPH", "", regex=False)
    return pd.to_numeric(cleaned, errors="coerce")


# 6. To transform `Number of Lanes` stored as text labels to numeric
def lanes_to_numeric(series):
    """'Two Lanes' -> 2, 'Six Lanes or More' -> 6, parking lot/unknown -> NaN."""
    lane_map = {
        "One Lane": 1,
        "Two Lanes": 2,
        "Three Lanes": 3,
        "Four Lanes": 4,
        "Five Lanes": 5,
        "Six Lanes or More": 6,
        "Not Applicable (Parking Lot)": np.nan,
        "CU is Unknown": np.nan,
        "Unknown": np.nan,
    }
    return series.map(lane_map)
