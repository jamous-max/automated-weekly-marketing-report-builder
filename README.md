# Automated Weekly Marketing Report Builder (V3.1)

## Overview

A modular Python automation system that processes marketing CSV exports, detects ISO weeks automatically, aggregates weekly KPIs, performs structured week-over-week analysis, and generates:

- A formatted TXT executive report
- A structured PDF performance report
- An AI-powered strategic executive summary

Version 3.1 introduces a more structured reporting flow, clearer weekly performance labeling, risk-aware summaries, and stronger control over AI-generated output.

This project demonstrates production-oriented AI integration with controlled architecture and cost governance.

**Note:** This public repository is a curated showcase version of the project. Some implementation details related to the final AI summary layer are intentionally simplified or withheld from the public version.

---

## What This Project Does

- Loads marketing performance CSV from the `input/` folder
- Cleans and standardizes:
  - Column names
  - Numeric fields
  - Date columns
  - Missing values
- Detects ISO weeks automatically
- Processes each week independently
- Skips weeks already processed (via history tracking)
- Aggregates weekly KPI totals
- Calculates derived KPI:
  - CTR (Click-Through Rate)
- Performs week-over-week comparison
- Classifies each week into:
  - Baseline
  - Growth
  - Performance Drop
  - Efficiency Drop
  - Mixed Signal
  - Stable
- Assigns risk level:
  - High
  - Medium
  - Low
- Generates structured AI executive summary
- Applies risk-sensitive tone modulation
- Generates formatted TXT and PDF reports
- Maintains `history.csv` to prevent duplicate processing

---

## Weekly Report Includes

For each detected ISO week, the system generates:

- `summary_week_X.txt`
- `summary_week_X.pdf`

Each PDF report includes:

- Report title
- Week number
- Reporting period
- Executive overview (AI-generated, structured)
- Week type classification
- Risk level tagging
- Aggregated KPI table:
  - Impressions
  - Clicks
  - CTR (%)
  - Conversions
  - Revenue

---

## AI Executive Summary (V3.1)

The executive summary layer is designed to produce short, structured, decision-friendly summaries based on weekly performance changes.

In this curated public version, the full prompt design and final AI summary logic are not included. The project structure still reflects the summary layer and how it fits into the reporting pipeline.

Architecture separation:

- Data Layer
- Comparison Layer
- Classification Layer
- AI Interpretation Layer

This separation helps keep the project modular, consistent, and easier to extend.

---

## Project Structure

```text
input/                      # Raw marketing CSV export
output/                     # Generated reports + history.csv

src/
├── config.py               # Paths and risk thresholds
├── loader.py               # Reads CSV files
├── cleaner.py              # Cleans and standardizes data
├── aggregator.py           # Aggregates numeric totals + CTR
├── comparison.py           # Week-over-week comparison + classification
├── history_logger.py       # Tracks processed weeks
├── ai_payload.py           # Builds structured KPI payload
├── ai_summary.py           # Public-safe executive summary layer
├── summary_report.py       # Generates formatted TXT report
├── pdf_report.py           # Generates formatted PDF report

main.py                     # Runs full reporting pipeline
```

---
## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your OpenAI API key as an environment variable

**Mac/Linux**

```bash
export OPENAI_API_KEY="your_key_here"
```

**Windows**

```bash
setx OPENAI_API_KEY "your_key_here"
```

### 3. Place CSV file inside

```
input/
```

### 4. Run

```bash
python main.py
```

Reports will be saved in:

```
output/
```

---

## Requirements

- Python 3.12 (recommended)
- pandas
- reportlab
- openai

---

## Future Improvements (Roadmap)

- Add CPA (Cost per Acquisition)
- Add ROAS calculation
- Add AOV tracking
- Add weighted risk scoring
- Add 4-week trend comparison
- Add token usage logging
- Add automation layer (n8n integration)
- Add dashboard interface
- Add error logging system

---

## Status

**Version 3.1** — Structured AI-assisted reporting engine with weekly performance labeling and risk-aware summaries.

_Last Updated: March 2026_