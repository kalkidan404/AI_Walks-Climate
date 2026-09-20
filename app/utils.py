import pandas as pd
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "processed_data"


def load_data():
    countries = {
        "Ethiopia": "ethiopia_clean.csv",
        "kenya": "kenya_clean.csv",
        "Sudan": "sudan_clean.csv",
        "Nigeria": "nigeria_clean.csv",
        "Tanzania": "tanzania_clean.csv",
    }

    dataframes = []

    for country, filename in countries.items():
        file_path = DATA_DIR / filename

        df = pd.read_csv(file_path)
        df["country"] = country

        dataframes.append(df)

    return pd.concat(dataframes, ignore_index=True)