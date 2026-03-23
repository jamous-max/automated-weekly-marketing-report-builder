import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Drop fully empty rows & duplicates
    df = df.dropna(how="all").drop_duplicates()

    # Clean numeric columns
    for col in df.columns:
        if df[col].dtype == object:
            # remove commas from numbers like "1,234"
            df[col] = df[col].str.replace(",", "")
            # try converting to numeric safely
            try:
                df[col] = pd.to_numeric(df[col])
            except Exception:
                pass  # leave it as-is if conversion fails

    # Parse date/time columns
    for col in df.columns:
        if "date" in col or "time" in col:
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass  # leave it as-is if conversion fails

    # Fill missing values
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(0)
        else:
            df[col] = df[col].fillna("")

    return df
