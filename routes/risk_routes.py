from flask import Blueprint, request, jsonify

from services.risk_engine import calculate_risk
from services.validator import validate_input
from services.financial_engine import calculate_financial_risk

from database.database import (
    save_risk_assessment,
    get_all_assessments,
    get_dashboard_summary,
    get_assessments_by_level,
    search_asset,
    update_risk_assessment,
    delete_risk_assessment
)

risk_bp = Blueprint("risk", __name__)


# -----------------------------
# Calculate Risk
# -----------------------------
@risk_bp.route("/calculate-risk", methods=["POST"])
def calculate():

    data = request.get_json()

    is_valid, error = validate_input(data)

    if not is_valid:
        return jsonify(error), 400

    risk_result = calculate_risk(data)

    financial_result = calculate_financial_risk(
        data["asset_value"],
        risk_result["risk_score"]
    )

    save_risk_assessment(
        asset_name=data["asset_name"],
        asset_value=data["asset_value"],
        risk_score=risk_result["risk_score"],
        risk_level=risk_result["risk_level"],
        estimated_loss=financial_result["estimated_financial_loss"]
    )

    return jsonify({
        "risk_assessment": risk_result,
        "financial_assessment": financial_result
    })


# -----------------------------
# Risk History
# -----------------------------
@risk_bp.route("/risk-history", methods=["GET"])
def risk_history():

    data = get_all_assessments()

    return jsonify(data)


# -----------------------------
# Dashboard
# -----------------------------
@risk_bp.route("/dashboard", methods=["GET"])
def dashboard():

    summary = get_dashboard_summary()

    return jsonify(summary)


# -----------------------------
# Filter Risk
# -----------------------------
@risk_bp.route("/filter-risk", methods=["GET"])
def filter_risk():

    level = request.args.get("level")

    if not level:
        return jsonify({
            "error": "Risk level is required"
        }), 400

    data = get_assessments_by_level(level)

    return jsonify(data)

@risk_bp.route("/search-asset", methods=["GET"])
def search():

    asset_name = request.args.get("name")

    if not asset_name:
        return jsonify({
            "error": "Asset name is required"
        }), 400

    data = search_asset(asset_name)

    return jsonify(data)

@risk_bp.route("/update-risk/<int:id>", methods=["PUT"])
def update_risk(id):

    data = request.get_json()

    risk_result = calculate_risk(data)

    financial_result = calculate_financial_risk(
        data["asset_value"],
        risk_result["risk_score"]
    )

    update_risk_assessment(
        id=id,
        asset_name=data["asset_name"],
        asset_value=data["asset_value"],
        risk_score=risk_result["risk_score"],
        risk_level=risk_result["risk_level"],
        estimated_loss=financial_result["estimated_financial_loss"]
    )

    return jsonify({
        "message": "Risk assessment updated successfully"
    })

@risk_bp.route("/delete-risk/<int:id>", methods=["DELETE"])
def delete_risk(id):

    delete_risk_assessment(id)

    return jsonify({
        "message": "Risk assessment deleted successfully"
    })