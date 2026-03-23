from src.comparison import (
    build_delta_summary,
    classify_risk,
    classify_week_type,
)


def generate_executive_summary(payload: dict, comparison: dict) -> str:
    """
    Public-safe fallback summary used in the curated portfolio version.
    """

    if not comparison.get("has_previous"):
        return (
            "Week Type: Baseline\n"
            "Risk Level: Low\n\n"
            "Performance Insight:\n"
            "This is the first recorded reporting period. "
            "It establishes a baseline for future comparison.\n\n"
            "Primary Driver:\n"
            "No historical benchmark available.\n\n"
            "Priority Focus:\n"
            "Monitor performance trends in the coming weeks."
        )

    revenue_change = comparison.get("revenue_change_pct")
    risk_level = classify_risk(revenue_change)
    week_type = classify_week_type(comparison)

    if revenue_change > 0:
        insight = "Performance improved compared to the previous week."
        focus = "Identify which campaigns drove the improvement and reinforce them."
    elif revenue_change < 0:
        insight = "Performance declined compared to the previous week."
        focus = "Investigate the channels contributing to the decline."
    else:
        insight = "Performance remained stable compared to the previous week."
        focus = "Monitor campaign efficiency and maintain consistency."

    return (
        f"Week Type: {week_type}\n"
        f"Risk Level: {risk_level}\n\n"
        f"Performance Insight:\n{insight}\n\n"
        f"Primary Driver:\nRevenue movement compared to previous week.\n\n"
        f"Priority Focus:\n{focus}"
    )


def generate_ai_executive_summary(payload: dict, comparison: dict) -> str:
    """
    Public portfolio version:
    The full prompt-based AI summary implementation is kept private.
    This placeholder preserves project structure while withholding
    the final prompt design and production summary logic.
    """
    return generate_executive_summary(payload, comparison)
