# 🌍 African Climate Dashboard

An interactive **Streamlit dashboard** built as part of my Python/data-analysis learning journey.

The dashboard takes the cleaned climate datasets from my African Climate EDA project and lets users interactively explore temperature, precipitation, and other climate variables across five African countries.

## 🎯 Purpose

The main goal of this project was to learn how to turn a Python data-analysis project into an **interactive web dashboard using Streamlit**.

Rather than only viewing charts generated in a Jupyter notebook, the dashboard allows the user to change filters and explore the data themselves.

## 🌍 Countries

The dashboard works with climate data for:

- Ethiopia
- Kenya
- Sudan
- Nigeria
- Tanzania

## 📊 Dashboard Features

### Country Selector

Users can select one or multiple countries using a sidebar multiselect.

### Year Range

Users can choose the range of years they want to explore using a slider.

### Variable Selector

Users can select between:

- `T2M` — Temperature at 2 meters
- `PRECTOTCORR` — Corrected precipitation
- `RH2M` — Relative humidity at 2 meters

### Temperature Trend

The dashboard displays the **monthly average temperature** for the selected countries and years.

Each country is represented by its own line, making it possible to compare temperature patterns over time.

### Precipitation Distribution

A boxplot shows the distribution of daily precipitation for the selected countries.

### Filtered Data

The dashboard also displays a sample of the filtered dataset so the user can see the underlying values.

---

# 🧠 What I Learned

This project was mainly about learning how **Streamlit connects Python code, user input, and data analysis**.

### Streamlit Basics

I learned how to:

```python
import streamlit as st
```

and use components such as:

```python
st.title()
st.write()
st.subheader()
st.dataframe()
```

### Page Configuration

I learned how to configure the Streamlit page:

```python
st.set_page_config(
    page_title="African Climate Dashboard",
    page_icon="🌍",
    layout="wide"
)
```

### Sidebar

I learned how to create interactive controls in the sidebar:

```python
st.sidebar.multiselect()
st.sidebar.slider()
st.sidebar.selectbox()
```

The important concept was that these widgets **return values** that can be stored in Python variables.

For example:

```python
selected_countries = st.sidebar.multiselect(
    "Select countries",
    countries,
    default=countries
)
```

The user's selections are then used to filter the DataFrame.

### Data Filtering

The selected controls are connected directly to Pandas:

```python
filtered_df = df[
    (df["country"].isin(selected_countries))
    & (df["YEAR"].between(selected_years[0], selected_years[1]))
]
```

This taught me how a user's interaction with a web interface can control a data-analysis operation.

### Visualization

I used Matplotlib to create:

- line charts
- boxplots

and displayed them through Streamlit using:

```python
st.pyplot(fig)
```

### Project Structure

I also learned to separate functionality instead of putting everything into one file.

```text
app/
├── main.py
└── utils.py
```

`main.py` handles the dashboard and user interface.

`utils.py` handles loading the data.

---

# 📁 Project Structure

```text
AI_Walks-Climate/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
│
├── scripts/
│   ├── __init__.py
│   └── README.md
│
├── data/
│   ├── raw_data/
│   └── processed_data/
│
├── notebooks/
│   ├── ethiopia_eda.ipynb
│   ├── kenya_eda.ipynb
│   ├── sudan_eda.ipynb
│   ├── nigeria_eda.ipynb
│   ├── tanzania_eda.ipynb
│   └── compare_countries.ipynb
│
├── requirements.txt
├── .gitignore
└── README.md
```

The `data/` directory is kept out of version control because the datasets are local project data.

---

# 🛠️ Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Jupyter Notebook
- Git & GitHub

---

# ▶️ Running the Dashboard Locally

Clone the repository:

```bash
git clone https://github.com/kalkidan404/AI_Walks-Climate.git
```

Move into the project:

```bash
cd AI_Walks-Climate
```

Create and activate the virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app/main.py
```

The dashboard will open in the browser.

---

# 🔗 How This Fits Into My Learning Journey

This dashboard comes after the exploratory data-analysis stage of the project.

```text
Raw climate data
       ↓
Data cleaning
       ↓
Exploratory data analysis
       ↓
Cross-country comparison
       ↓
Python visualizations
       ↓
Streamlit dashboard
```

The important progression for me was moving from:

> **"I can analyze data in a notebook."**

to:

> **"I can turn that analysis into something another person can interact with."**

---

# 🚀 Future Improvements

Possible future improvements include:

- additional interactive visualizations
- climate indicators for extreme events
- summary statistics that update with the filters
- correlation analysis
- improved dashboard layout
- deployment to Streamlit Community Cloud
- dynamically fetching data instead of relying on local files

Deployment is intentionally left as a future step while I continue learning the fundamentals of data analysis and Streamlit.

---

# 📌 Learning Outcome

This project helped me understand the basics of building interactive data applications with Python and Streamlit.

The main takeaway:

> **Pandas analyzes the data, Matplotlib visualizes it, and Streamlit turns the analysis into an interactive application.**
> the visual streamlit :

## 📊 Dashboard

![African Climate Dashboard](image\photo_2026-09-21_14-26-22.jpg)
