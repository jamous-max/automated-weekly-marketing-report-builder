# Automated Weekly Marketing Report Builder (V2.2)

## Overview

Python automation project that loads marketing CSV exports, cleans and standardizes the data, detects ISO weeks automatically, aggregates weekly KPIs, and generates both:

- A structured, human-readable TXT report
- A formatted PDF performance report

The pipeline runs end-to-end and processes multiple weeks from a single CSV file automatically — no manual Excel calculations required.



## What This Project Does

- Loads marketing performance CSV from the `input/` folder
- Cleans and standardizes:
  - Column names
  - Numeric fields
  - Date columns
  - Missing values
- Detects ISO weeks inside the dataset
- Processes each week separately
- Skips weeks that were already processed (using a history file)
- Aggregates totals for numeric KPIs per week
- Calculates derived KPI:
  - CTR (Click-Through Rate)
- Performs week-over-week comparison
- Generates a structured executive-style summary
- Applies consistent number formatting across TXT and PDF reports
- Maintains a `history.csv` file to prevent duplicate processing



## Weekly Report Includes

For each detected ISO week, the system generates:

- `summary_week_X.txt`
- `summary_week_X.pdf`

Each PDF report includes:

- Report title
- Week number
- Reporting period
- Executive overview paragraph
- Aggregated KPI table (Impressions, Clicks, CTR (%), Conversions, Revenue)



## Project Structure

```
input/                      # Raw marketing CSV export
output/                     # Generated reports + history.csv

src/
├── config.py               # Stores paths and settings
├── loader.py               # Reads CSV files
├── cleaner.py              # Cleans and standardizes data
├── aggregator.py           # Aggregates numeric totals and calculates CTR
├── comparison.py           # Week-over-week comparison logic
├── history_logger.py       # Tracks processed weeks
├── ai_payload.py           # Builds structured KPI payload
├── ai_summary.py           # Generates executive summary text
├── summary_report.py       # Generates formatted TXT report
├── pdf_report.py           # Generates formatted PDF report

main.py                     # Runs the full reporting pipeline
```


## How to Run

1. Install dependencies:
pip install -r requirements.txt
(Or manually install pandas and reportlab.)

2. Place a CSV file inside:
input/

3. Run:
python main.py

Reports and history will be saved inside:
output/



## Requirements

- Python 3.12 (recommended)
- pandas
- reportlab



## Notes

CSV file must include:

- A `date` column
- Numeric KPI columns (Impressions, Clicks, Conversions, Revenue)

Features:

- Automatic ISO week detection
- Multi-week processing from a single CSV
- Incremental history tracking
- Duplicate prevention
- Derived KPI calculation (CTR)
- Structured executive summary generation
- Modular project structure for future enhancements



## Status

Version 2.2 — Multi-week processing with week-over-week comparison and structured reporting.

Last Updated: February 2026