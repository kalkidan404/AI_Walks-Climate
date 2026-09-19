# 🌍 African Climate EDA — COP32

A data analysis project exploring climate patterns across five African countries using historical climate data from **2015–2026**.

The project focuses on **data profiling, cleaning, exploratory data analysis (EDA), cross-country climate comparison, and interactive visualization with Streamlit**. The goal is to turn raw climate data into meaningful insights that can help explain differences in temperature, precipitation, extreme heat, and drought patterns across the region.

---

## 📌 Project Overview

Climate change does not affect every region in the same way. Different countries experience different combinations of heat, rainfall variability, drought, and other climate stresses.

This project analyzes climate data from:

- 🇪🇹 Ethiopia
- 🇰🇪 Kenya
- 🇸🇩 Sudan
- 🇳🇬 Nigeria
- 🇹🇿 Tanzania

The analysis covers the period **2015–2026**.

The project follows a complete data-analysis workflow:

```text
Raw Climate Data
       ↓
Data Profiling
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Cross-Country Comparison
       ↓
Statistical Analysis
       ↓
Climate Insights
       ↓
Interactive Streamlit Dashboard
```

---

# 🎯 Project Objectives

The main objectives are to:

1. Clean and prepare climate datasets from five African countries.
2. Explore temperature and precipitation patterns.
3. Identify extreme heat and prolonged dry periods.
4. Compare climate indicators across countries.
5. Use statistical analysis to examine differences in temperature.
6. Present the findings through an interactive Streamlit dashboard.
7. Frame the findings in the context of climate vulnerability and COP32.

---

# 📊 Climate Variables

The datasets contain several climate variables, including:

| Variable      | Description                     |
| ------------- | ------------------------------- |
| `T2M`         | Average temperature at 2 meters |
| `T2M_MAX`     | Maximum temperature             |
| `T2M_MIN`     | Minimum temperature             |
| `T2M_RANGE`   | Daily temperature range         |
| `PRECTOTCORR` | Corrected precipitation         |
| `RH2M`        | Relative humidity               |
| `WS2M`        | Wind speed at 2 meters          |
| `WS2M_MAX`    | Maximum wind speed              |
| `PS`          | Surface pressure                |
| `QV2M`        | Specific humidity               |
| `YEAR`        | Year                            |
| `DOY`         | Day of year                     |

Additional variables were created during preprocessing:

- `country`
- `date`
- `month`
- `extreme_heat`
- `dry_day`

---

# 🧹 Data Cleaning & Preparation

Before analysis, the raw datasets were processed to make them suitable for comparison.

The cleaning process included:

### 1. Adding country information

Each dataset was assigned its corresponding country.

```python
df["country"] = "Ethiopia"
```

### 2. Creating dates

The original data contained `YEAR` and `DOY` (day of year), which were converted into actual dates.

```python
df["date"] = pd.to_datetime(
    df["YEAR"] * 1000 + df["DOY"],
    format="%Y%j"
)
```

### 3. Creating the month variable

```python
df["month"] = df["date"].dt.month
```

This allowed monthly climate patterns to be analyzed.

### 4. Handling missing values

Missing-value codes such as `-999` were replaced with `NaN`.

```python
df.replace(-999, np.nan, inplace=True)
```

### 5. Removing duplicates

Duplicate observations were identified and removed.

```python
df.drop_duplicates(inplace=True)
```

### 6. Missing-value analysis

Missing percentages were calculated for the variables to identify columns requiring attention.

### 7. Outlier analysis

Z-scores were used to identify unusually extreme observations.

```python
Z_score = (
    df[cols] - df[cols].mean()
) / df[cols].std()
```

Climate outliers were not automatically removed because extreme values can represent genuine climate events.

---

# 🔎 Exploratory Data Analysis

The project examines several major climate patterns.

## 🌡️ Temperature Trends

Monthly average `T2M` was calculated for each country.

The analysis includes:

- monthly temperature trends
- mean temperature
- median temperature
- standard deviation
- comparison between countries

A line chart is used to visualize monthly average temperature from **2015–2026**.

---

## 🌧️ Precipitation Variability

`PRECTOTCORR` was analyzed to understand rainfall patterns and variability.

The analysis includes:

- mean precipitation
- median precipitation
- standard deviation
- precipitation distributions
- comparison between countries

Side-by-side boxplots are used to compare precipitation distributions across the five countries.

---

# 🔥 Extreme Heat

Extreme heat was defined as:

```python
df["extreme_heat"] = df["T2M_MAX"] > 35
```

The number of extreme-heat days was calculated for each country and year.

This helps identify countries experiencing more frequent days above the selected temperature threshold.

---

# ☀️ Drought / Dry Spells

A dry day was defined as:

```python
df["dry_day"] = df["PRECTOTCORR"] < 1
```

The analysis then identifies the longest consecutive sequence of dry days within each year.

This provides an indicator of prolonged dry conditions rather than simply counting individual dry days.

---

# 📈 Cross-Country Comparison

The five cleaned datasets are combined into a single dataframe to allow direct comparison.

```python
df = pd.concat(
    [ethiopia, kenya, sudan, nigeria, tanzania],
    ignore_index=True
)
```

The comparison includes:

- temperature
- precipitation
- extreme heat
- dry spells
- climate variability

---

# 🧪 Statistical Analysis

A one-way ANOVA was performed to test whether mean temperature differs between the five countries.

The test produced:

```text
F-statistic: 18938.75
p-value: < 0.001
```

The result provides strong statistical evidence that mean `T2M` differs among the five countries.

However, ANOVA only indicates that at least one group differs. It does not identify which specific pairs of countries differ.

A post-hoc test such as **Tukey's HSD** would be required for pairwise comparisons.

---

# 🌍 Key Climate Findings

The analysis shows substantial differences in climate characteristics across the five countries.

### Temperature

The countries have noticeably different average temperature profiles.

For example:

- Ethiopia has a mean `T2M` of approximately **16.07°C**.
- Nigeria has a mean of approximately **26.66°C**.
- Tanzania has a mean of approximately **26.80°C**.
- Sudan has a mean of approximately **28.76°C**.

---

### Precipitation

Rainfall variability also differs between countries.

For example:

- Ethiopia: approximately **6.29 mm/day** standard deviation
- Nigeria: approximately **7.27 mm/day**
- Sudan: approximately **3.06 mm/day**
- Tanzania: approximately **8.00 mm/day**

These differences demonstrate that the countries experience different precipitation regimes.

---

### Extreme Heat

Sudan stands out strongly in the analyzed extreme-heat indicator.

The dataset records approximately:

**224.5 extreme-heat days per year**

using the `T2M_MAX > 35°C` threshold.

The other countries recorded substantially fewer such days under this definition.

---

### Dry Spells

Sudan also shows substantially longer maximum consecutive dry periods.

The average maximum annual dry spell was approximately:

- Ethiopia — **37.9 days**
- Nigeria — **35.8 days**
- Sudan — **142.8 days**
- Tanzania — **40.3 days**

These indicators highlight substantial differences in exposure to heat and prolonged dryness.

---

# 🌐 COP32 Context

The findings are intended to provide a data-driven view of climate exposure across the countries studied.

The analysis suggests that climate stress takes different forms across the region:

- temperature exposure
- rainfall variability
- extreme heat
- prolonged dry periods

The results should not be interpreted as a complete measure of climate vulnerability.

Climate vulnerability also depends on factors such as:

- population exposure
- socioeconomic conditions
- infrastructure
- agricultural dependence
- access to resources
- adaptive capacity
- existing climate policies

Therefore, the climate indicators in this project provide **evidence about climate exposure**, rather than a complete vulnerability assessment.

---

# 🖥️ Streamlit Dashboard

The next stage of the project is an interactive **Streamlit dashboard**.

The dashboard will allow users to explore the climate data without directly interacting with the notebooks.

Planned features include:

### Country Selection

Users will be able to select one or more countries:

```text
☑ Ethiopia
☑ Kenya
☑ Sudan
☑ Nigeria
☑ Tanzania
```

### Temperature Analysis

Interactive visualizations for:

- monthly average temperature
- temperature distributions
- yearly temperature patterns
- country comparison

### Precipitation Analysis

Interactive visualizations for:

- monthly precipitation
- precipitation distributions
- rainfall variability
- country comparison

### Climate Extremes

Indicators for:

- extreme-heat days
- longest dry spells
- yearly climate extremes

### Statistical Summary

The dashboard will display summary statistics such as:

- mean
- median
- standard deviation
- minimum
- maximum

### Interactive Exploration

Users will be able to change:

- country
- year range
- climate variable
- visualization

and explore the dataset dynamically.

---

# 🛠️ Technologies

The project uses:

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **SciPy**
- **Jupyter Notebook**
- **Streamlit**
- **Git**
- **GitHub**

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/kalkidan404/AI_Walks-Climate.git
```

Move into the project:

```bash
cd AI_Walks-Climate
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

# 📋 Requirements

The project's Python dependencies are:

```text
numpy
pandas
matplotlib
scipy
pytest
streamlit
```

---

# 🚀 Running the Streamlit App

Once the dashboard has been implemented:

```bash
streamlit run app.py
```

Streamlit will start a local development server and provide a URL that can be opened in the browser.

---

# 📁 Project Structure

```text
AI_Walks-Climate/
│
├── data/
│   ├── raw_data/
│   │   └── ...
│   │
│   └── processed_data/
│       ├── ethiopia_clean.csv
│       ├── kenya_clean.csv
│       ├── sudan_clean.csv
│       ├── nigeria_clean.csv
│       └── tanzania_clean.csv
│
├── notebooks/
│   ├── ethiopia_eda.ipynb
│   ├── kenya_eda.ipynb
│   ├── sudan_eda.ipynb
│   ├── nigeria_eda.ipynb
│   ├── tanzania_eda.ipynb
│   └── compare_countries.ipynb
│
├── tests/
│
├── app.py
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

---

# 🔄 Git Workflow

The project uses Git branches to organize development.

A typical workflow is:

```text
Create branch
     ↓
Develop feature
     ↓
Commit changes
     ↓
Push branch
     ↓
Open Pull Request
     ↓
Review
     ↓
Merge into main
```

Examples:

```bash
git checkout -b eda-ethiopia
```

```bash
git add .
git commit -m "Complete Ethiopia EDA"
```

```bash
git push origin eda-ethiopia
```

---

# 📚 Project Learning Goals

This project is also part of a broader learning journey into **data analysis and AI**.

Through the project, the main skills being practiced are:

- Python
- Pandas
- NumPy
- data cleaning
- exploratory data analysis
- data visualization
- statistical analysis
- Git/GitHub
- Jupyter
- Streamlit
- communicating data insights

The goal is not simply to produce charts, but to learn the complete process of going from:

```text
Raw Data
   ↓
Clean Data
   ↓
Analysis
   ↓
Evidence
   ↓
Insight
   ↓
Interactive Application
```

---

# 🌱 Future Improvements

Possible future additions include:

- interactive map visualizations
- additional African countries
- more climate variables
- advanced statistical tests
- correlation analysis
- trend analysis
- climate anomaly detection
- downloadable reports
- Streamlit deployment
- additional socioeconomic indicators
- integration of external climate-vulnerability datasets

---

# 📌 Conclusion

This project demonstrates how climate data can be transformed from raw observations into interpretable evidence.

By combining **data cleaning, exploratory analysis, statistical testing, visualization, and an interactive Streamlit dashboard**, the project provides a practical framework for comparing climate patterns across African countries.

The analysis also demonstrates an important principle in data science:

> **Data can reveal patterns, but the quality of a conclusion depends on the quality and scope of the evidence behind it.**

The climate indicators analyzed here provide one part of the picture. A broader assessment of climate vulnerability would require combining climate exposure with socioeconomic, infrastructural, and adaptive-capacity data.
