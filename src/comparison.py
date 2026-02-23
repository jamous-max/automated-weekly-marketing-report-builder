# src/comparison.py

import csv
from pathlib import Path
from typing import Optional


HISTORY_FILE = Path("output/history.csv")


def _pct_change(current: float, previous: float) -> Optional[float]:
    if previous in (0, None):
        return None
    return ((current - previous) / previous) * 100


def _load_previous_week(current_week: int) -> Optional[dict]:
    if not HISTORY_FILE.exists():
        return None

    rows = []

    with open(HISTORY_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    if not rows:
        return None

    # Convert week numbers to int
    for row in rows:
        row["week_number"] = int(row["week_number"])

    previous_weeks = [r for r in rows if r["week_number"] < current_week]

    if not previous_weeks:
        return None

    # Get latest previous week
    previous = max(previous_weeks, key=lambda r: r["week_number"])

    # Convert numeric fields
    numeric_fields = [
        "impressions",
        "clicks",
        "ctr",
        "conversions",
        "revenue",
    ]

    for field in numeric_fields:
        previous[field] = float(previous[field])

    return previous


def compare_with_previous_week(current_payload: dict) -> dict:
    current_week = current_payload["week_number"]

    previous = _load_previous_week(current_week)

    if not previous:
        return {"has_previous": False}

    comparison = {
        "has_previous": True,
        "impressions_change_pct": _pct_change(
            current_payload["impressions"], previous["impressions"]
        ),
        "clicks_change_pct": _pct_change(
            current_payload["clicks"], previous["clicks"]
        ),
        "ctr_change_pct": _pct_change(
            current_payload["ctr"], previous["ctr"]
        ),
        "conversions_change_pct": _pct_change(
            current_payload["conversions"], previous["conversions"]
        ),
        "revenue_change_pct": _pct_change(
            current_payload["revenue"], previous["revenue"]
        ),
        "previous_week_number": previous["week_number"],
    }

    return comparison