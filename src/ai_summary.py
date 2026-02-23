def generate_executive_summary(payload: dict, comparison: dict) -> str:
    """
    Generate executive summary text using KPI payload
    and week-over-week comparison data.
    """

    week = payload["week_number"]
    start = payload["report_start"]
    end = payload["report_end"]

    impressions = payload["impressions"]
    clicks = payload["clicks"]
    conversions = payload["conversions"]
    revenue = payload["revenue"]

    # ---- First week case (no comparison available) ----
    if not comparison.get("has_previous"):
        return (
            f"Week {week} ({start} to {end}) delivered "
            f"{impressions:,} impressions, {clicks:,} clicks, "
            f"and {conversions:,} conversions, generating revenue of {revenue:,}. "
            "As this is the first recorded reporting period, "
            "no historical comparison is available. "
            "This baseline will serve as a reference for future performance evaluation."
        )

    # ---- Comparison case ----
    revenue_change = comparison.get("revenue_change_pct")
    conversions_change = comparison.get("conversions_change_pct")
    ctr_change = comparison.get("ctr_change_pct")

    previous_week = comparison.get("previous_week_number")

    def direction_text(value):
        if value is None:
            return "remained stable"
        elif value > 0:
            return f"increased by {abs(value):.1f}%"
        elif value < 0:
            return f"decreased by {abs(value):.1f}%"
        else:
            return "remained stable"

    revenue_direction = direction_text(revenue_change)
    conversions_direction = direction_text(conversions_change)
    ctr_direction = direction_text(ctr_change)

    summary = (
        f"Week {week} ({start} to {end}) generated {impressions:,} impressions "
        f"and {clicks:,} clicks, resulting in {conversions:,} conversions "
        f"and revenue of {revenue:,}. "
        f"Compared to Week {previous_week}, revenue {revenue_direction}, "
        f"conversions {conversions_direction}, and click-through rate {ctr_direction}. "
        "Overall, performance reflects current momentum relative to the prior reporting period."
    )

    return summary