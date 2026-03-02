from openai import OpenAI
from src.comparison import (
    build_delta_summary,
    classify_risk,
    classify_week_type,
)

client = OpenAI()


def generate_ai_executive_summary(payload: dict, comparison: dict) -> str:
    """
    Generate structured executive summary using OpenAI (V3).
    Deterministic classification + structured AI interpretation.
    """

    # ---- Baseline Case (First Week) ----
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

    # ---- Deterministic Layer ----
    delta_summary = build_delta_summary(comparison)

    revenue_change = comparison.get("revenue_change_pct")
    risk_level = classify_risk(revenue_change)

    week_type = classify_week_type(comparison)

    # ---- Structured Prompt (V3) ----
    # ---- Tone Adjustment Based on Risk ----
    if risk_level == "High":
        tone_instruction = (
            "Use firm and decisive tone."
            "Clearly state the material impact of the decline."
            "Emphasize immediate corrective action."
            "Avoid dramatic or emotional language. "
        )
    else:
        tone_instruction = (
            "Maintain calm and strategic tone. " "Focus on clarity and prioritization."
        )

    # ---- Structured Prompt (V3.1 with Tone Control) ----
    prompt = f"""
ROLE:
You are a senior growth strategist writing for a busy marketing manager.

INPUT:
Week Type: {week_type}
Risk Level: {risk_level}
Performance Summary:
{delta_summary}

TASK:
Explain the performance clearly and concisely.
Identify the main driver.
State what requires attention.
Recommend one clear focus.

TONE:
{tone_instruction}

OUTPUT FORMAT:

Week Type: {week_type}
Risk Level: {risk_level}

Performance Insight:
(1–2 short sentences explaining what changed and why it matters.)

Primary Driver:
(1 short sentence.)

Priority Focus:
(1 clear action direction.)

RULES:
- Use simple, direct English.
- Short sentences.
- No jargon.
- No hedging words.
- Do NOT repeat raw numbers.
- Max 120 tokens.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        max_output_tokens=130,
    )

    return response.output_text.strip()
