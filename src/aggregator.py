import pandas as pd


def aggregate_data(dataframes: list[pd.DataFrame]) -> pd.DataFrame:
    """
    Combine cleaned dataframes and calculate total metrics.
    """

    if not dataframes:
        return pd.DataFrame()

    # 1. Combine all data into one DataFrame
    combined_df = pd.concat(dataframes, ignore_index=True)

    # 2. Select numeric columns only
    numeric_columns = combined_df.select_dtypes(include="number")

    # 3. Sum numeric values
    totals = numeric_columns.sum().to_frame(name="total").reset_index()

    # Rename for clarity
    totals.columns = ["metric", "value"]

    return totals
