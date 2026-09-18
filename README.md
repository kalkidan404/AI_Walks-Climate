# 🌍 African Climate EDA — COP32

An exploratory data analysis project examining climate patterns across **Ethiopia, Kenya, Uganda, Tanzania, and Rwanda** using daily climate data from 2015–2026.

The project focuses on understanding temperature, precipitation, humidity, wind, and other climate variables through data cleaning, statistical analysis, visualization, and cross-country comparison.

---

## 📌 Project Overview

This project was developed as a data analysis exercise to explore climate conditions across five African countries and identify patterns that may be relevant to climate vulnerability discussions leading up to **COP32**.

The analysis follows a complete data workflow:

```text
Raw Climate Data
       ↓
Data Loading
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Statistical Analysis
       ↓
Visualization
       ↓
Country Comparison
       ↓
Climate Insights
```

Each country is analyzed separately before the cleaned datasets are combined for cross-country comparison.

---

## 🌍 Countries Analyzed

- 🇪🇹 Ethiopia
- 🇰🇪 Kenya
- 🇺🇬 Uganda
- 🇹🇿 Tanzania
- 🇷🇼 Rwanda

The datasets contain daily observations covering approximately **2015–2026**.

---

## 📊 Dataset Variables

The climate datasets contain variables including:

| Variable      | Description                        | Unit   |
| ------------- | ---------------------------------- | ------ |
| `YEAR`        | Year of observation                | —      |
| `DOY`         | Day of year                        | —      |
| `T2M`         | Mean daily air temperature at 2m   | °C     |
| `T2M_MAX`     | Maximum daily temperature          | °C     |
| `T2M_MIN`     | Minimum daily temperature          | °C     |
| `T2M_RANGE`   | Daily temperature range            | °C     |
| `PRECTOTCORR` | Bias-corrected total precipitation | mm/day |
| `RH2M`        | Relative humidity at 2m            | %      |
| `WS2M`        | Mean wind speed at 2m              | m/s    |
| `WS2M_MAX`    | Maximum wind speed at 2m           | m/s    |
| `PS`          | Atmospheric surface pressure       | kPa    |
| `QV2M`        | Specific humidity                  | g/kg   |

---

# 🧹 Data Cleaning

The same cleaning workflow was applied to each country's dataset.

### 1. Load the dataset

```python
df = pd.read_csv("../data/raw_data/ethiopia (1).csv")
```

The file path was changed accordingly for each country.

### 2. Add country information

```python
df["country"] = "Ethiopia"
```

This allows the datasets to later be combined while retaining the country associated with each observation.

### 3. Create a datetime column

The original dataset contains `YEAR` and `DOY` rather than a standard date.

```python
df["date"] = pd.to_datetime(
    df["YEAR"] * 1000 + df["DOY"],
    format="%Y%j"
)
```

A separate month column was then extracted:

```python
df["month"] = df["date"].dt.month
```

### 4. Handle missing values

The datasets use `-999` as a missing-value sentinel.

```python
df.replace(-999, np.nan, inplace=True)
```

Missing values were then investigated using:

```python
df.isna().sum()
```

and:

```python
df.isna().mean() * 100
```

Rows with more than 30% missing values were identified and removed where necessary, while remaining weather-variable missing values were handled using forward filling.

### 5. Remove duplicate rows

```python
df.duplicated().sum()
```

Duplicate observations were removed with:

```python
df.drop_duplicates(inplace=True)
```

---

# 📈 Exploratory Data Analysis

The analysis examined several aspects of the climate data.

## Summary Statistics

`df.describe()` was used to examine:

- mean
- standard deviation
- minimum
- maximum
- quartiles
- median

This provided an initial understanding of the distribution and variability of each climate variable.

---

# 🌡️ Temperature Analysis

Monthly average `T2M` was calculated using:

```python
monthly_t2m = (
    df.groupby(["YEAR", "month"])["T2M"]
    .mean()
    .reset_index()
)
```

A datetime column was then created to produce a continuous time series.

The resulting line chart shows monthly temperature patterns throughout the 2015–2026 period.

The warmest and coolest months were identified using:

```python
peak_tempMax = monthly_t2m.loc[
    monthly_t2m["T2M"].idxmax()
]

peak_tempMin = monthly_t2m.loc[
    monthly_t2m["T2M"].idxmin()
]
```

The analysis also examined whether temperatures showed obvious long-term increases, decreases, or unusual fluctuations.

---

# 🌧️ Precipitation Analysis

Monthly precipitation was analyzed to identify rainfall patterns and seasonal variation.

For calendar-month analysis across the entire period:

```python
monthly_prec = (
    df.groupby(["month"])["PRECTOTCORR"]
    .sum()
    .reset_index()
)
```

The analysis examined:

- overall rainfall distribution
- rainy periods
- peak rainfall months
- relatively dry periods
- seasonal variation

Precipitation was also examined at the daily level to understand how rainfall is distributed across individual days.

---

# 📉 Outlier Detection

Z-scores were calculated for the major climate variables:

```python
cols = [
    "T2M",
    "T2M_MAX",
    "T2M_MIN",
    "PRECTOTCORR",
    "RH2M",
    "WS2M",
    "WS2M_MAX"
]

Z_score = (
    df[cols] - df[cols].mean()
) / df[cols].std()
```

Rows containing values with:

```text
|Z| > 3
```

were flagged as potential outliers.

Outliers were **retained rather than automatically removed** because an extreme climate observation may represent a genuine weather event rather than an error.

---

# 🔗 Correlation Analysis

A correlation matrix was created for the numeric variables.

```python
numeric_df = df.select_dtypes(include="number")

correlation = numeric_df.corr()
```

The correlation matrix was visualized using a heatmap.

Correlation values range from:

```text
-1 ←──────── 0 ────────→ +1
negative       none       positive
```

The analysis was used to identify strong relationships between variables such as:

- temperature and specific humidity
- specific humidity and relative humidity
- humidity and daily temperature range

Correlation was interpreted as **association rather than causation**.

---

# 🔵 Relationship Analysis

Scatter plots were used to investigate relationships between individual variables.

### Temperature vs Relative Humidity

```python
plt.scatter(
    df["T2M"],
    df["RH2M"]
)
```

### Temperature Range vs Wind Speed

```python
plt.scatter(
    df["T2M_RANGE"],
    df["WS2M"]
)
```

These plots provide a visual representation of whether the variables show positive, negative, or weak relationships.

---

# 📊 Distribution Analysis

The distribution of daily precipitation was examined using a histogram.

```python
plt.hist(
    df["PRECTOTCORR"].dropna(),
    bins=30
)
```

Because precipitation can contain many low-rainfall observations and fewer heavy-rainfall events, the distribution was also considered for a logarithmic scale where appropriate.

The analysis focused on identifying:

- skewness
- concentration of observations
- variability
- extreme rainfall events

---

# 🫧 Bubble Chart

A bubble chart was used to examine the relationship between temperature and relative humidity while representing precipitation using bubble size.

```python
plt.scatter(
    df["T2M"],
    df["RH2M"],
    s=df["PRECTOTCORR"] * 10,
    alpha=0.5
)
```

Here:

```text
X-axis       → Temperature
Y-axis       → Relative Humidity
Bubble size  → Precipitation
```

This allows three variables to be explored in a single visualization.

---

# 🌍 Cross-Country Comparison

After completing the individual country analyses, the cleaned datasets were combined into a single DataFrame.

The comparison examines:

### Temperature

- monthly average temperature
- overall mean
- median
- standard deviation
- temperature trends over time

### Precipitation

- precipitation distributions
- mean
- median
- standard deviation
- rainfall variability

### Extreme Events

- days where `T2M_MAX > 35°C`
- consecutive dry days where `PRECTOTCORR < 1 mm`

### Statistical Testing

Where appropriate, statistical tests such as:

- one-way ANOVA
- Kruskal–Wallis

can be used to determine whether observed differences between countries are statistically significant.

---

# 📁 Project Structure

```text
AI-Walks-Climate/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   └── raw_data/
│       ├── ethiopia.csv
│       ├── kenya.csv
│       ├── uganda.csv
│       ├── tanzania.csv
│       └── rwanda.csv
│
├── notebooks/
│   ├── ethiopia_eda.ipynb
│   ├── kenya_eda.ipynb
│   ├── uganda_eda.ipynb
│   ├── tanzania_eda.ipynb
│   ├── rwanda_eda.ipynb
│   └── compare_countries.ipynb
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

> File names may differ slightly depending on the local dataset names.

---

# 🐍 Technologies Used

- **Python**
- **Jupyter Notebook**
- **Pandas** — data manipulation and analysis
- **NumPy** — numerical operations
- **Matplotlib** — data visualization
- **Seaborn** — statistical visualization
- **Git & GitHub** — version control
- **GitHub Actions** — continuous integration

---

# ⚙️ Setup

Clone the repository:

```bash
git clone <repository-url>
cd AI-Walks-Climate
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Start Jupyter:

```bash
jupyter notebook
```

or:

```bash
jupyter lab
```

---

# 📦 Requirements

The main Python dependencies are:

```text
numpy
pandas
matplotlib
seaborn
jupyter
```

---

# 🔀 Git Workflow

The project uses separate branches for different stages of the analysis.

Example country branches:

```text
eda-ethiopia
eda-kenya
eda-uganda
eda-tanzania
eda-rwanda
```

The cross-country analysis uses:

```text
compare-countries
```

This keeps the country-specific analysis separate before the datasets are synthesized.

---

# 🔒 Data & Git

Raw and cleaned CSV files are excluded from GitHub where appropriate.

The repository focuses on:

- analysis notebooks
- code
- documentation
- visualizations
- reproducible methodology

rather than storing large datasets directly in the repository.

---

# 🎯 Project Goals

The main goals of this project are to demonstrate the ability to:

- load and understand real-world datasets
- clean missing and duplicate data
- work with dates and time series
- calculate summary statistics
- detect and interpret outliers
- analyze correlations
- create meaningful visualizations
- interpret distributions
- compare multiple datasets
- communicate findings through data

More broadly, the project is an introduction to using **Python for real-world data analysis** and forms part of a larger journey toward **data science and AI**.

---

# 📌 Key Takeaway

This project moves beyond simply creating graphs.

The workflow is:

```text
Understand the data
        ↓
Clean the data
        ↓
Explore the data
        ↓
Find relationships
        ↓
Visualize patterns
        ↓
Interpret the results
        ↓
Compare countries
        ↓
Communicate evidence
```

The objective is to turn raw climate observations into **clear, reproducible, evidence-based insights**.

---

## 📚 References

- NASA POWER — Climate and meteorological data
- World Bank Climate Change Knowledge Portal
- IPCC — Climate Change Assessment Reports
- World Meteorological Organization — Climate Reports
- Python, Pandas, NumPy, Matplotlib, and Seaborn documentation
