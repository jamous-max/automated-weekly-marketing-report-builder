def build_ai_payload(totals_df, week_number, start_date, end_date):
    """
    Convert aggregated totals into a structured dictionary
    for AI executive summary generation.
    """
    
    payload = {
        "week_number": week_number,
        "report_start": start_date.strftime("%Y-%m-%d"),
        "report_end": end_date.strftime("%Y-%m-%d"),
    }

    # Add KPI values dynamically
    for _, row in totals_df.iterrows():
        metric = row["metric"].lower()
        value = row["value"]

        # Normalize key names
        if metric == "ctr (%)":
            payload["ctr"] = round(value, 2)
        else:
            payload[metric] = int(value)
    
    
    return payload
