import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from utils import load_data


# -----------------------------
# Page setup
# -----------------------------

st.set_page_config(
    page_title="African Climate Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 African Climate Dashboard")
st.write(
    "Explore temperature, precipitation, and climate patterns "
    "across five African countries."
)


# -----------------------------
# Load data
# -----------------------------

df = load_data()


# -----------------------------
# Sidebar filters
# -----------------------------

st.sidebar.header("Filters")

countries = sorted(df["country"].unique())

selected_countries = st.sidebar.multiselect(
    "Select countries",
    countries,
    default=countries
)

min_year = int(df["YEAR"].min())
max_year = int(df["YEAR"].max())

selected_years = st.sidebar.slider(
    "Select year range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

variable = st.sidebar.selectbox(
    "Select variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)


# -----------------------------
# Filter data
# -----------------------------

filtered_df = df[
    (df["country"].isin(selected_countries))
    & (df["YEAR"].between(selected_years[0], selected_years[1]))
]


# -----------------------------
# Temperature trend
# -----------------------------

st.subheader("🌡️ Temperature Trend")

monthly_t2m = (
    filtered_df
    .groupby(["country", "YEAR", "Month"])["T2M"]
    .mean()
    .reset_index()
)

monthly_t2m["date"] = pd.to_datetime(
    monthly_t2m["YEAR"].astype(str)
    + "-"
    + monthly_t2m["Month"].astype(str)
    + "-01"
)

fig, ax = plt.subplots(figsize=(12, 5))

for country in selected_countries:
    country_data = monthly_t2m[
        monthly_t2m["country"] == country
    ]

    ax.plot(
        country_data["date"],
        country_data["T2M"],
        label=country
    )

ax.set_xlabel("Year")
ax.set_ylabel("Average Temperature (°C)")
ax.set_title("Monthly Average Temperature")
ax.legend()
ax.grid(True)

st.pyplot(fig)


# -----------------------------
# Precipitation distribution
# -----------------------------

st.subheader("🌧️ Precipitation Distribution")

fig, ax = plt.subplots(figsize=(10, 5))

boxplot_data = [
    filtered_df[
        filtered_df["country"] == country
    ]["PRECTOTCORR"].dropna()
    for country in selected_countries
]

ax.boxplot(
    boxplot_data,
    tick_labels=selected_countries
)

ax.set_xlabel("Country")
ax.set_ylabel("Precipitation (mm/day)")
ax.set_title("Precipitation Distribution")

st.pyplot(fig)


# -----------------------------
# Selected variable
# -----------------------------

st.subheader(f"📊 {variable}")

st.write(
    f"Showing **{variable}** for the selected countries "
    f"and years."
)

st.dataframe(
    filtered_df[
        ["country", "YEAR", "Month", variable]
    ].head(100)
)