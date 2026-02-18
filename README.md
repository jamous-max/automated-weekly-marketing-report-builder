# Automated Weekly Marketing Report Builder (V2)

## Overview

Python automation project that loads marketing CSV exports, cleans and standardizes the data, aggregates total KPIs, and generates both:

* A simple human-readable **TXT report**
* A structured, client-ready **PDF performance report**

The pipeline runs end-to-end and processes multiple CSV files automatically — no manual Excel calculations required.


## What This Project Does

* Loads all CSV exports from the input folder
* Cleans and standardizes:

  * Column names
  * Numeric fields
  * Date columns
  * Missing values
* Automatically detects reporting period:

  * Start date (earliest date in data)
  * End date (latest date in data)
  * ISO week number
* Aggregates totals for all numeric KPIs
* Generates:

  * Simple TXT summary report
  * Professional PDF report with:

    * Report title
    * Week number
    * Reporting period
    * KPI summary table
* Saves reports to the output folder
* Works as a **modular, maintainable automation pipeline**


## Example Output (PDF Report Includes)

* Weekly Marketing Performance Report
* Week number (auto-detected)
* Reporting period (auto-calculated from CSV data)
* Aggregated KPI table (Impressions, Clicks, Conversions, Revenue, etc.)


## Project Structure

```
input/                    # Raw CSV exports
output/                   # Generated reports

src/config.py             # Stores paths and settings
src/loader.py             # Reads CSV files
src/cleaner.py            # Cleans and standardizes data
src/aggregator.py         # Aggregates numeric totals
src/summary_report.py     # Generates TXT report
src/pdf_report.py         # Generates formatted PDF report

main.py                   # Runs the full pipeline
```


## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

(Or manually install `pandas` and `reportlab`)

2. Place CSV files inside:

```
input/
```

3. Run:

```bash
python main.py
```

4. Reports will be saved inside:

```
output/
```

## Requirements

* Python 3.10+
* pandas
* reportlab


## Notes

* CSV files must include at least:

  * A date column (`date`)
  * Numeric KPI columns
* The reporting period is automatically calculated from the data
* Supports multiple CSV files per run
* Designed as a modular automation foundation for further enhancements (e.g., AI-generated executive summaries, workflow automation)


## Status

Version 2 — Structured reporting with dynamic date intelligence and PDF generation.

**Last Updated:** February 2026