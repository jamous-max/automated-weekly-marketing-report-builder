from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FOLDER = BASE_DIR / "input"
OUTPUT_FOLDER = BASE_DIR / "output"

# Risk Classification Thresholds
# ==============================

# Revenue drop thresholds
HIGH_RISK_REVENUE_DROP = 0.10  # 10% drop
MEDIUM_RISK_REVENUE_DROP = 0.05  # 5% drop

# CPA increase thresholds
HIGH_RISK_CPA_INCREASE = 0.20  # 20% increase
MEDIUM_RISK_CPA_INCREASE = 0.10  # 10% increase

# Optional (future growth classification)
GROWTH_CONVERSION_INCREASE = 0.05
GROWTH_REVENUE_INCREASE = 0.05
