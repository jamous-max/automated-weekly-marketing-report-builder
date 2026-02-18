import pandas as pd
from pathlib import Path
from config import INPUT_FOLDER
from config import OUTPUT_FOLDER
from src.loader import load_csv_files
from src.cleaner import clean_dataframe
from src.aggregator import aggregate_data
from src.pdf_report import generate_pdf_report   
from src.summary_report import save_summary_report


def main():
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    # 1. Load CSV files
    dataframes = load_csv_files(INPUT_FOLDER)

    # 2. Clean each dataframe
    cleaned_dfs = [clean_dataframe(df) for df in dataframes]

    # Combine cleaned dataframes to compute reporting period
    combined_df = pd.concat(cleaned_dfs, ignore_index=True)

    #Extract date info from combined data
    start_date = combined_df["date"].min()
    end_date = combined_df["date"].max()

    week_number = start_date.isocalendar().week

    #Format Dates
    start_date_str = start_date.strftime("%b %d, %Y")
    end_date_str = end_date.strftime("%b %d, %Y")


    # 3. Aggregate totals
    totals_df = aggregate_data(cleaned_dfs)
    
    # 4. Save summary report as PDF
    output_file = OUTPUT_FOLDER / "summary_report.pdf"
    generate_pdf_report(
    totals_df,
    output_file,
    week_number=week_number,
    start_date=start_date_str,
    end_date=end_date_str
)
    # 5. Save summary report as TXT
    txt_file = OUTPUT_FOLDER / "summary_report.txt"
    save_summary_report(totals_df, txt_file)


    print(f"Reports saved to {OUTPUT_FOLDER}")

if __name__ == "__main__":
    main()
