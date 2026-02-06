from pathlib import Path
from config import INPUT_FOLDER
from config import OUTPUT_FOLDER
from src.loader import load_csv_files
from src.cleaner import clean_dataframe
from src.aggregator import aggregate_data
from src.summary_report import save_summary_report


def main():
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    # 1. Load CSV files
    dataframes = load_csv_files(INPUT_FOLDER)

    # 2. Clean each dataframe
    cleaned_dfs = [clean_dataframe(df) for df in dataframes]

    # 3. Aggregate totals
    totals_df = aggregate_data(cleaned_dfs)

    # 4. Save summary report as text
    output_file = OUTPUT_FOLDER / "summary_report.txt"
    save_summary_report(totals_df, output_file)

    print(f"Report saved to {output_file}")

if __name__ == "__main__":
    main()
