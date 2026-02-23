import pandas as pd
from pathlib import Path


def log_week_history(payload: dict, history_path: Path):
    """
    Append weekly aggregated data to history CSV.
    Creates the file if it does not exist.
    """

    # Convert payload dict to DataFrame (single row)
    new_row = pd.DataFrame([payload])

    # If file exists, append
    if history_path.exists():
        existing = pd.read_csv(history_path)
        updated = pd.concat([existing, new_row], ignore_index=True)
        updated.to_csv(history_path, index=False)
    else:
        new_row.to_csv(history_path, index=False)