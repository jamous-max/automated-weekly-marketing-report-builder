from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def generate_pdf_report(
    totals_df, output_path, week_number, start_date, end_date, executive_summary
):

    doc = SimpleDocTemplate(str(output_path))
    elements = []

    styles = getSampleStyleSheet()

    # ---- Title ----
    title = Paragraph("<b>Weekly Marketing Performance Report</b>", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 0.5 * inch))

    # ---- Reporting Period ----
    period_info = Paragraph(
        f"<b>Week {week_number}</b><br/>"
        f"Reporting Period: {start_date} - {end_date}",
        styles["Normal"],
    )
    elements.append(period_info)
    elements.append(Spacer(1, 0.3 * inch))

    # ---- Executive Overview ----
    executive_title = Paragraph("<b>Executive Overview</b>", styles["Heading2"])
    elements.append(executive_title)
    elements.append(Spacer(1, 0.2 * inch))

    # ---- Structured Executive Summary Rendering ----
    summary_lines = executive_summary.split("\n")

    for line in summary_lines:

        if not line.strip():
            elements.append(Spacer(1, 0.2 * inch))
            continue

        # Bold section headers
        if (
            line.startswith("Week Type:")
            or line.startswith("Risk Level:")
            or line.startswith("Performance Insight:")
            or line.startswith("Primary Driver:")
            or line.startswith("Priority Focus:")
        ):
            elements.append(Paragraph(f"<b>{line}</b>", styles["Normal"]))
        else:
            elements.append(Paragraph(line, styles["Normal"]))

        elements.append(Spacer(1, 0.15 * inch))

    elements.append(Spacer(1, 0.4 * inch))

    # ---- Performance Table ----
    table_data = [["Metric", "Value"]]

    for _, row in totals_df.iterrows():
        metric_name = row["metric"]
        value = row["value"]

        if metric_name.lower() != "ctr (%)":
            metric_name = metric_name.replace("_", " ").title()

        if metric_name.lower() == "ctr (%)":
            formatted_value = f"{value:.2f}%"
        else:
            formatted_value = f"{int(value):,}"

        table_data.append([metric_name, formatted_value])

    table = Table(table_data, colWidths=[3 * inch, 2 * inch])

    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 11),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ]
        )
    )

    elements.append(table)

    doc.build(elements)
