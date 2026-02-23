import pandas as pd
from pathlib import Path
from config import INPUT_FOLDER, OUTPUT_FOLDER
from src.loader import load_csv_files
from src.cleaner import clean_dataframe
from src.aggregator import aggregate_data
from src.pdf_report import generate_pdf_report
from src.summary_report import save_summary_report
from src.ai_payload import build_ai_payload
from src.ai_summary import generate_executive_summary
from src.history_logger import log_week_history
from src.comparison import compare_with_previous_week


def main():
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    # 1️ Load single CSV
    dataframes = load_csv_files(INPUT_FOLDER)

    if not dataframes:
        print("No CSV files found.")
        return

    df = clean_dataframe(dataframes[0])

    # 2️ Add ISO week column
    iso_calendar = df["date"].dt.isocalendar()
    df["week_number"] = iso_calendar.week.astype(int)

    
    # 3️ Detect unique weeks
    unique_weeks = sorted(df["week_number"].unique())

    # 4️ Load history (if exists)
    history_file = OUTPUT_FOLDER / "history.csv"

    if history_file.exists():
        history_df = pd.read_csv(history_file)
        processed_weeks = set(history_df["week_number"].astype(int))
    else:
        processed_weeks = set()

    # 5️ Process each week
    for week in unique_weeks:

        if week in processed_weeks:
            print(f"Week {week} already processed — skipping.")
            continue

        week_df = df[df["week_number"] == week]

        # Aggregate
        totals_df = aggregate_data([week_df])

        # Reporting period for this week only
        start_date = week_df["date"].min()
        end_date = week_df["date"].max()

        start_date_str = start_date.strftime("%b %d, %Y")
        end_date_str = end_date.strftime("%b %d, %Y")

        
        # Build payload
        payload = build_ai_payload(
            totals_df,
            week,
            start_date,
            end_date
        )

        
        # Compare BEFORE logging
        comparison = compare_with_previous_week(payload)

        # Generate executive summary
        executive_summary = generate_executive_summary(payload, comparison)

        # File paths
        txt_path = OUTPUT_FOLDER / f"summary_week_{week}.txt"
        pdf_path = OUTPUT_FOLDER / f"summary_week_{week}.pdf"

        # Save TXT
        save_summary_report(
            executive_summary,
            totals_df,
            txt_path,
            week,
            start_date_str,
            end_date_str
        )

        # Save PDF
        generate_pdf_report(
            totals_df,
            pdf_path,
            week_number=week,
            start_date=start_date_str,
            end_date=end_date_str,
            executive_summary=executive_summary
        )

        # Log history LAST
        log_week_history(payload, history_file)

        print(f"Week {week} processed successfully.")

    print(f"All reports saved to {OUTPUT_FOLDER}")


if __name__ == "__main__":
    main()