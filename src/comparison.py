# src/comparison.py

import csv
from pathlib import Path
from typing import Optional

from config import (
    HIGH_RISK_REVENUE_DROP,
    MEDIUM_RISK_REVENUE_DROP,
)

HISTORY_FILE = Path("output/history.csv")


# Percentage Change Calculation


def _pct_change(current: float, previous: float) -> Optional[float]:
    if previous in (0, None):
        return None
    return ((current - previous) / previous) * 100


# Load Previous Week


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

    for row in rows:
        row["week_number"] = int(row["week_number"])

    previous_weeks = [r for r in rows if r["week_number"] < current_week]

    if not previous_weeks:
        return None

    previous = max(previous_weeks, key=lambda r: r["week_number"])

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


# Week-over-Week Comparison


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
        "clicks_change_pct": _pct_change(current_payload["clicks"], previous["clicks"]),
        "ctr_change_pct": _pct_change(current_payload["ctr"], previous["ctr"]),
        "conversions_change_pct": _pct_change(
            current_payload["conversions"], previous["conversions"]
        ),
        "revenue_change_pct": _pct_change(
            current_payload["revenue"], previous["revenue"]
        ),
        "previous_week_number": previous["week_number"],
    }

    return comparison


# Delta Summary Builder (for AI input)


def build_delta_summary(comparison: dict) -> str:
    if not comparison.get("has_previous"):
        return "No previous week data available."

    lines = []

    def format_change(label, value):
        if value is None:
            return None
        elif value > 0:
            return f"{label} increased by {abs(value):.1f}%."
        elif value < 0:
            return f"{label} decreased by {abs(value):.1f}%."
        else:
            return f"{label} remained stable."

    mapping = {
        "Impressions": comparison.get("impressions_change_pct"),
        "Clicks": comparison.get("clicks_change_pct"),
        "Conversions": comparison.get("conversions_change_pct"),
        "Revenue": comparison.get("revenue_change_pct"),
        "CTR": comparison.get("ctr_change_pct"),
    }

    for label, value in mapping.items():
        sentence = format_change(label, value)
        if sentence:
            lines.append(sentence)

    return " ".join(lines)


# Risk Classification (Revenue-Based)


def classify_risk(revenue_change_pct: Optional[float]) -> str:
    if revenue_change_pct is None:
        return "Low"

    # Thresholds in config are decimals (0.10 = 10%)
    high_threshold = HIGH_RISK_REVENUE_DROP * 100
    medium_threshold = MEDIUM_RISK_REVENUE_DROP * 100

    if revenue_change_pct <= -high_threshold:
        return "High"
    elif revenue_change_pct <= -medium_threshold:
        return "Medium"
    else:
        return "Low"


# Week Type Classification


def classify_week_type(comparison: dict) -> str:
    if not comparison.get("has_previous"):
        return "Baseline"

    revenue_change = comparison.get("revenue_change_pct")
    conversions_change = comparison.get("conversions_change_pct")
    impressions_change = comparison.get("impressions_change_pct")

    if revenue_change is None or conversions_change is None:
        return "Stable"

    # 1️ Strong Growth
    if revenue_change > 0 and conversions_change > 0:
        return "Growth"

    # 2️ Clear Performance Drop
    if revenue_change < 0 and conversions_change < 0:
        return "Performance Drop"

    # 3️ Efficiency Drop (traffic up, results down)
    if impressions_change and impressions_change > 0 and conversions_change < 0:
        return "Efficiency Drop"

    # 4️ Mixed signal
    if (revenue_change > 0 and conversions_change < 0) or (
        revenue_change < 0 and conversions_change > 0
    ):
        return "Mixed Signal"

    return "Stable"
