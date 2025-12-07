import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Alabama Crash Severity Dashboard", layout="wide")


@st.cache_data
def load_data():
    return pd.read_pickle("data/cleaned/crash_2018_cleaned.pkl")


df = load_data()

# Prepare fields used later
severity_map = {"PDO": 1, "Minor": 2, "Serious": 3, "Fatal": 4}
df["Severity_Num"] = df["Crash Severity"].map(severity_map)
if "log_AADT" not in df.columns and "AADT" in df.columns:
    df["log_AADT"] = np.log1p(df["AADT"])

st.sidebar.title("Crash Severity Dashboard")
page = st.sidebar.radio("Go to", ["🏠 Home", "📊 Overview", "📈 Severity Distribution", "📋 Factor Ranking"])

# 0) WELCOME PAGE ------------------------------------------------------------
if page == "🏠 Home":
    st.title("🚦Alabama Crash Data Dashboard")

    st.markdown("""
    ### 👋 About This App
    This interactive dashboard was created to help researchers, students, and transportation professionals:
    - Explore Alabama crash data using visual analytics  
    - Understand the distribution of crash severity  
    - Investigate contributing factors (driver, vehicle, roadway, environment)  
    - Support data-driven safety analysis and decision making  

    ### 📅 Data Used
    - **Year:** 2018  
    - **Source:** ALDOT 
    - **Cleaned dataset:** crash_2018_cleaned.pkl  

    ### 👨‍💻 Developers
    - **Md Roknuzzaman**
    - **Kwaku Emmanuel Tufuor**
   

    ### 📌 How to use this app
    Use the **left sidebar** to navigate:
    - **Overview** – dataset preview & severity distribution  
    - **Severity distribution** – filter crashes and visualize severity  
    - **Factor ranking** – identify variables most related to severity  

    ---
    **Start exploring using the sidebar**
    """)


# 1) OVERVIEW ---------------------------------------------------------------
elif page == "📊 Overview":
    st.title("Overview of Alabama 2018 Crash Data")

    st.write("Rows, columns:", df.shape)

    st.subheader("Sample of dataset")
    st.dataframe(df.head())

    st.subheader("Crash severity distribution (%)")
    sev_counts = df["Crash Severity"].value_counts(normalize=True) * 100
    st.bar_chart(sev_counts)


# 2) SEVERITY DISTRIBUTION --------------------------------------------------
elif page == "📈 Severity Distribution":
    st.title("Crash severity distribution")

    st.sidebar.subheader("Filters: Crash Type, Area and Time")

    county = st.sidebar.selectbox(
        "County", ["All"] + sorted(df["County"].dropna().unique().tolist())
    )
    at = st.sidebar.selectbox(
        "Area Type", ["All"] + sorted(df["Area Type"].dropna().unique().tolist())
    )
    tod = st.sidebar.selectbox(
        "Time of Day", ["All"] + sorted(df["Time of Day"].dropna().unique().tolist())
    )
    cmr = st.sidebar.selectbox(
        "Crash Manner", ["All"] + sorted(df["Crash Manner Recode"].dropna().unique().tolist())
    )

    st.sidebar.subheader("Filters: Vehicle and Driver")

    vtype = st.sidebar.selectbox(
        "Vehicle Type", ["All"] + sorted(df["Vehicle Type Recode"].dropna().unique().tolist())
    )
    dlv = st.sidebar.selectbox(
        "Driving License Validity",
        ["All"] + sorted(df["Driver License Validity"].dropna().unique().tolist()),
    )
    dui = st.sidebar.selectbox(
        "DUI", ["All"] + sorted(df["BAC Available"].dropna().unique().tolist())
    )
    gender = st.sidebar.selectbox(
        "Driver Gender", ["All"] + sorted(df["Driver Gender Recode"].dropna().unique().tolist())
    )

    st.sidebar.subheader("Filters: Roadway and Environment")

    fc = st.sidebar.selectbox(
        "Functional Class",
        ["All"] + sorted(df["Functional Class Recode"].dropna().unique().tolist()),
    )
    curve = st.sidebar.selectbox(
        "Curvature", ["All"] + sorted(df["Curvature"].dropna().unique().tolist())
    )
    grade = st.sidebar.selectbox("Grade", ["All"] + sorted(df["Grade"].dropna().unique().tolist()))
    vis = st.sidebar.selectbox(
        "Visibility Obstructed",
        ["All"] + sorted(df["Visibility Obstruction Recode"].dropna().unique().tolist()),
    )
    light = st.sidebar.selectbox(
        "Lighting Condition",
        ["All"] + sorted(df["Lighting Conditions Recode"].dropna().unique().tolist()),
    )

    subset = df.copy()
    if county != "All":
        subset = subset[subset["County"] == county]
    if tod != "All":
        subset = subset[subset["Time of Day"] == tod]
    if vtype != "All":
        subset = subset[subset["Vehicle Type Recode"] == vtype]
    if at != "All":
        subset = subset[subset["Area Type"] == at]
    if cmr != "All":
        subset = subset[subset["Crash Manner Recode"] == cmr]
    if dlv != "All":
        subset = subset[subset["Driver License Validity"] == dlv]
    if dui != "All":
        subset = subset[subset["BAC Available"] == dui]
    if gender != "All":
        subset = subset[subset["Driver Gender Recode"] == gender]
    if fc != "All":
        subset = subset[subset["Functional Class Recode"] == fc]
    if curve != "All":
        subset = subset[subset["Curvature"] == curve]
    if grade != "All":
        subset = subset[subset["Grade"] == grade]
    if vis != "All":
        subset = subset[subset["Visibility Obstruction Recode"] == vis]
    if light != "All":
        subset = subset[subset["Lighting Conditions Recode"] == light]

    st.write(f"Number of crashes in selection: {len(subset)}")

    if len(subset) > 0:
        # counts and %
        sev_counts = subset["Crash Severity"].value_counts()
        sev_pct = (sev_counts / sev_counts.sum() * 100).round(1)
        sev_table = pd.DataFrame({"Count": sev_counts, "Percent": sev_pct})

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Crash severity table")
            st.dataframe(sev_table)

        with col2:
            st.subheader("Crash severity pie")
            fig, ax = plt.subplots(figsize=(4, 4))
            wedges, _ = ax.pie(
                sev_counts.values,
                labels=None,
                startangle=90,
            )
            ax.axis("equal")
            ax.set_title("Crash severity share")
            # separate legend on the side
            ax.legend(
                wedges,
                sev_counts.index,
                title="Crash severity",
                loc="center left",
                bbox_to_anchor=(1.05, 0.5),
            )
            st.pyplot(fig)
    else:
        st.warning("No data for this selection.")


# 3) FACTOR RANKING ---------------------------------------------------------
elif page == "📋 Factor Ranking":
    st.title("Ranking of factors related to crash severity")

    st.sidebar.subheader("Filters: Crash Type, Area and Time")

    county = st.sidebar.selectbox(
        "County", ["All"] + sorted(df["County"].dropna().unique().tolist())
    )
    at = st.sidebar.selectbox(
        "Area Type", ["All"] + sorted(df["Area Type"].dropna().unique().tolist())
    )
    tod = st.sidebar.selectbox(
        "Time of Day", ["All"] + sorted(df["Time of Day"].dropna().unique().tolist())
    )
    cmr = st.sidebar.selectbox(
        "Crash Manner", ["All"] + sorted(df["Crash Manner Recode"].dropna().unique().tolist())
    )

    st.sidebar.subheader("Filters: Vehicle and Driver")

    vtype = st.sidebar.selectbox(
        "Vehicle Type", ["All"] + sorted(df["Vehicle Type Recode"].dropna().unique().tolist())
    )
    dlv = st.sidebar.selectbox(
        "Driving License Validity",
        ["All"] + sorted(df["Driver License Validity"].dropna().unique().tolist()),
    )
    dui = st.sidebar.selectbox(
        "DUI", ["All"] + sorted(df["BAC Available"].dropna().unique().tolist())
    )
    gender = st.sidebar.selectbox(
        "Driver Gender", ["All"] + sorted(df["Driver Gender Recode"].dropna().unique().tolist())
    )

    st.sidebar.subheader("Filters: Roadway and Environment")

    fc = st.sidebar.selectbox(
        "Functional Class",
        ["All"] + sorted(df["Functional Class Recode"].dropna().unique().tolist()),
    )
    curve = st.sidebar.selectbox(
        "Curvature", ["All"] + sorted(df["Curvature"].dropna().unique().tolist())
    )
    grade = st.sidebar.selectbox("Grade", ["All"] + sorted(df["Grade"].dropna().unique().tolist()))
    vis = st.sidebar.selectbox(
        "Visibility Obstructed",
        ["All"] + sorted(df["Visibility Obstruction Recode"].dropna().unique().tolist()),
    )
    light = st.sidebar.selectbox(
        "Lighting Condition",
        ["All"] + sorted(df["Lighting Conditions Recode"].dropna().unique().tolist()),
    )

    # Apply same filters to a working copy
    sub = df.copy()
    if county != "All":
        sub = sub[sub["County"] == county]
    if tod != "All":
        sub = sub[sub["Time of Day"] == tod]
    if vtype != "All":
        sub = sub[sub["Vehicle Type Recode"] == vtype]
    if at != "All":
        sub = sub[sub["Area Type"] == at]
    if cmr != "All":
        sub = sub[sub["Crash Manner Recode"] == cmr]
    if dlv != "All":
        sub = sub[sub["Driver License Validity"] == dlv]
    if dui != "All":
        sub = sub[sub["BAC Available"] == dui]
    if gender != "All":
        sub = sub[sub["Driver Gender Recode"] == gender]
    if fc != "All":
        sub = sub[sub["Functional Class Recode"] == fc]
    if curve != "All":
        sub = sub[sub["Curvature"] == curve]
    if grade != "All":
        sub = sub[sub["Grade"] == grade]
    if vis != "All":
        sub = sub[sub["Visibility Obstruction Recode"] == vis]
    if light != "All":
        sub = sub[sub["Lighting Conditions Recode"] == light]

    st.write(f"Number of crashes in selection: {len(sub)}")

    # Variables to use in ranking
    cat_for_corr = [
        "Area Type",
        "Time of Day",
        "Curvature",
        "Grade",
        "Vehicle Type Recode",
        "BAC Available",
    ]
    num_vars = ["log_AADT", "Speed Limit Num", "Impact Speed Num", "Driver Age"]

    if len(sub) > 100:
        dummies = pd.get_dummies(sub[cat_for_corr], drop_first=True)

        corr_with_sev = pd.concat([sub[["Severity_Num"] + num_vars], dummies], axis=1).corr()

        corr_sev = corr_with_sev["Severity_Num"].drop(labels=["Severity_Num"])
        corr_abs = corr_sev.abs().sort_values(ascending=False)

        fig, ax = plt.subplots(figsize=(6, 5))
        sns.barplot(
            x=corr_abs.values,
            y=corr_abs.index,
            orient="h",
            color="steelblue",
            ax=ax,
        )
        ax.set_xlabel("|Correlation with severity|")
        ax.set_ylabel("|Factors|")
        ax.set_title("Factor ranking (selected subset)")
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.warning("Not enough crashes in this subset to compute a stable ranking.")

