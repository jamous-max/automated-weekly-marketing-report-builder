def save_summary_report(totals_df, output_path):
    """
    Prepare a human-readable text summary and save it to a file.
    """
    if totals_df.empty:
        report_text = "No data available."
    else:
        lines = ["Summary Marketing Report — Totals\n"]

        for _, row in totals_df.iterrows():
            metric_name = row["metric"]
            value = row["value"]

            # Keep CTR fully uppercase
            if metric_name.lower() != "ctr (%)":
                metric_name = metric_name.replace("_", " ").title()

            # Format values properly
            if metric_name.lower() == "ctr (%)":
                formatted_value = f"{value:.2f}%"
            else:
                formatted_value = f"{int(value):,}"

            lines.append(f"{metric_name}: {formatted_value}")

        report_text = "\n".join(lines)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    return output_path
