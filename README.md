# Automated Weekly Marketing Report Builder (V1)

## Overview

Python automation project that loads marketing CSV exports, cleans them, aggregates totals, and saves a human-readable text report.
The pipeline runs end-to-end, processing multiple CSV files automatically without needing manual calculations.

This project is a learning project to practice working with CSV files, cleaning data, aggregating numbers, and organizing a Python automation pipeline.


## What this project does

* Loads all CSV exports from the input folder
* Cleans and standardizes the data (column names, numeric values, dates, missing values)
* Aggregates totals for all numeric columns
* Builds a simple text report summarizing totals
* Saves the report to the output folder
* Works end-to-end as a **modular, easy-to-own pipeline**


## Project Structure

input/ — folder where raw CSV exports are placed
output/ — folder where summary text reports are saved

src/config.py — stores paths and settings
src/loader.py — reads CSV files from input folder
src/cleaner.py — cleans and standardizes the data
src/aggregator.py — aggregates totals for numeric columns
src/summary_report.py — builds and saves human-readable text report
main.py — starts the pipeline program
```

## How to run the project

1. Make sure Python is installed
2. Place CSV files in `input/raw_exports/`
3. Run the program:

```bash
python main.py
```

4. The pipeline will load, clean, aggregate, and save a text report to `output/weekly_report.txt`


## Notes

* The text report shows **totals for all numeric metrics** in a readable format
* This is **V1** — the first working version of the pipeline
* CSV files must have at least one date column (`date`) and numeric metrics


**Last updated:** February 2026