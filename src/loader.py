import pandas as pd
from pathlib import Path


def load_csv_files(folder_path):
    folder_path = Path(folder_path)
    dataframes = []

    for file in folder_path.glob("*.csv"):
        df = pd.read_csv(file)   # <-- Make sure you actually read CSV
        dataframes.append(df)

    return dataframes
