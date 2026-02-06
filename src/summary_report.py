def save_summary_report(totals_df, output_path):
    """
    Prepare a human-readable text summary and save it to a file.
    """
    if totals_df.empty:
        report_text = "No data available."
    else:
        lines = ["Summary Marketing Report — Totals\n"]
        for _, row in totals_df.iterrows():
            metric_name = row["metric"].replace("_", " ").title()
            value = round(row["value"], 2)
            lines.append(f"{metric_name}: {value}")
        report_text = "\n".join(lines)

    # Write to text file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    return output_path
