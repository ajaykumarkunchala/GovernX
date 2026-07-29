# services/financial_engine.py

def calculate_financial_risk(asset_value, risk_score):

    # Estimated loss based on risk percentage
    estimated_loss = (asset_value * risk_score) / 100

    return {
        "asset_value": asset_value,
        "risk_percentage": f"{risk_score}%",
        "estimated_financial_loss": estimated_loss
    }