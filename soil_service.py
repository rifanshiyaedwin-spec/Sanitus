"""
soil_service.py - Soil Health NPK & pH Recommendation Engine
Analyzes soil test values (pH, Nitrogen, Phosphorus, Potassium)
and calculates organic and chemical fertilizer requirements per acre.
"""

def analyze_soil_health(ph, nitrogen, phosphorus, potassium, field_area_acres=1.0):
    """
    Evaluates soil parameters and calculates recommended fertilizer dosage.
    """
    insights = []
    recommendations = []

    # 1. Soil pH Evaluation
    if ph < 6.0:
        insights.append("Soil is Acidic (pH < 6.0). Micronutrient availability is restricted.")
        recommendations.append({
            "type": "Organic Amendment",
            "name": "Agricultural Lime (Calcium Carbonate)",
            "dosage": f"{int(50 * field_area_acres)} kg",
            "reason": "Raises soil pH to optimal 6.5 neutral range."
        })
    elif ph > 7.5:
        insights.append("Soil is Alkaline (pH > 7.5). Risk of Iron & Zinc chlorosis.")
        recommendations.append({
            "type": "Organic Amendment",
            "name": "Gypsum or Elemental Sulfur",
            "dosage": f"{int(25 * field_area_acres)} kg",
            "reason": "Lowers soil alkalinity and improves drainage."
        })
    else:
        insights.append("Soil pH is in the Optimal Range (6.0 - 7.5).")

    # 2. Nitrogen (N) Evaluation
    if nitrogen < 140:
        insights.append("🔴 Nitrogen Deficiency Detected (<140 mg/kg). Causes leaf yellowing.")
        recommendations.append({
            "type": "Chemical Fertilizer",
            "name": "Urea (46% N)",
            "dosage": f"{int(25 * field_area_acres)} kg per acre",
            "reason": "Restores vegetative growth and leaf greenness."
        })
        recommendations.append({
            "type": "Organic Solution",
            "name": "Neem-Coated Vermicompost",
            "dosage": f"{int(200 * field_area_acres)} kg per acre",
            "reason": "Slow-release nitrogen with bio-protection."
        })
    else:
        insights.append("✔ Nitrogen levels are Adequate.")

    # 3. Phosphorus (P) Evaluation
    if phosphorus < 25:
        insights.append("🟡 Phosphorus Deficiency (<25 mg/kg). Restricts root establishment.")
        recommendations.append({
            "type": "Chemical Fertilizer",
            "name": "Single Super Phosphate (SSP)",
            "dosage": f"{int(30 * field_area_acres)} kg per acre",
            "reason": "Promotes root expansion and flowering."
        })

    # 4. Potassium (K) Evaluation
    if potassium < 120:
        insights.append("🟡 Potassium Deficiency (<120 mg/kg). Weakens disease resistance.")
        recommendations.append({
            "type": "Chemical Fertilizer",
            "name": "Muriate of Potash (MOP / 60% K)",
            "dosage": f"{int(15 * field_area_acres)} kg per acre",
            "reason": "Enhances crop fruit quality and drought tolerance."
        })

    return {
        "ph_status": "Acidic" if ph < 6.0 else ("Alkaline" if ph > 7.5 else "Optimal"),
        "insights": insights,
        "recommendations": recommendations
    }
