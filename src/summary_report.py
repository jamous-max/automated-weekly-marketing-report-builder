def save_summary_report(
    executive_summary,
    totals_df,
    output_path,
    week_number,
    start_date,
    end_date
):
    """
    Generate executive-style text summary and save to file.
    """

    lines = [
        f"Summary Marketing Report — Week {week_number}",
        f"Reporting Period: {start_date} – {end_date}",
        "",
        "Executive Overview:",
        executive_summary,
        "",
        "Performance Breakdown:",
        ""
    ]

    if totals_df.empty:
        lines.append("No data available.")
    else:
        for _, row in totals_df.iterrows():
            metric_name = row["metric"]
            value = row["value"]

            if metric_name.lower() != "ctr (%)":
                metric_name = metric_name.replace("_", " ").title()

            if metric_name.lower() == "ctr (%)":
                formatted_value = f"{value:.2f}%"
            else:
                formatted_value = f"{int(value):,}"

            lines.append(f"{metric_name}: {formatted_value}")

    report_text = "\n".join(lines)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    return output_path