from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def generate_pdf_report(totals_df, output_path, week_number, start_date, end_date):


    doc = SimpleDocTemplate(str(output_path))
    elements = []

    styles = getSampleStyleSheet()

    # ---- Title ----
    title = Paragraph("<b>Weekly Marketing Performance Report</b>", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 0.5 * inch))

    # --- Date ----
    period_info = Paragraph(
    f"<b>Week {week_number}</b><br/>"
    f"Reporting Period: {start_date} - {end_date}",
    styles["Normal"]
)

    elements.append(period_info)
    elements.append(Spacer(1, 0.2 * inch))



    # ---- Description ----
    description = Paragraph(
    "This report summarizes total marketing performance metrics "
    "aggregated from all campaign data for the selected reporting period.",
    styles["Normal"]
)

    elements.append(description)
    elements.append(Spacer(1, 0.2 * inch))


    # ---- Table Data ----
    table_data = [["Metric", "Value"]]

    for _, row in totals_df.iterrows():
        table_data.append([row["metric"].capitalize(), f"{row['value']:,}"])

    table = Table(table_data, colWidths=[3 * inch, 2 * inch])

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 11),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ]))

    elements.append(table)

    doc.build(elements)
