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
    totals = numeric_columns.sum().to_frame(name="value").reset_index()

    # Rename for clarity
    totals.columns = ["metric", "value"]

    # 4. Calculate CTR if possible
    impressions = totals.loc[totals["metric"] == "impressions", "value"].values
    clicks = totals.loc[totals["metric"] == "clicks", "value"].values

    

    if len(impressions) > 0 and len(clicks) > 0 and impressions[0] != 0:
        ctr = round((clicks[0] / impressions[0]) * 100, 2)

        ctr_row = pd.DataFrame([{
            "metric": "CTR (%)",
            "value": ctr
        }])

        # Insert CTR after Clicks
        click_index = totals.index[totals["metric"] == "clicks"].tolist()
        if click_index:
            insert_position = click_index[0] + 1
            totals = pd.concat([
                totals.iloc[:insert_position],
                ctr_row,
                totals.iloc[insert_position:]
            ]).reset_index(drop=True)

    return totals
