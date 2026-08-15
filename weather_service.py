"""
weather_service.py - Weather Intelligence & Disease Risk Forecasting Service
Provides real-time agricultural weather metrics, spraying safety advisories,
and humidity-driven fungal disease risk assessments.
"""

import numpy as np

def get_weather_forecast(location="Green Valley Farm"):
    """
    Simulate real-time agricultural weather parameters and risk metrics.
    """
    # Deterministic simulation with natural variation
    humidity = float(np.random.randint(75, 95))
    temperature_c = float(np.random.randint(22, 32))
    wind_speed_kmh = float(np.random.randint(5, 18))
    rain_forecast = "YES (Rain expected in 12 hours)" if humidity > 82 else "NO (Clear Sky)"
    
    # Spraying recommendation
    if humidity > 85 or "YES" in rain_forecast:
        spray_advisory = "⚠ Delay spraying! High humidity / rain expected. Fungicide may wash off."
        spray_status = "DELAY"
    else:
        spray_advisory = "✔ Favorable conditions for spraying. Apply in early morning."
        spray_status = "SAFE"

    # Disease Risk Forecasting
    powdery_mildew_risk = round(min(98.0, humidity * 1.05), 1)
    late_blight_risk = round(min(95.0, (humidity + temperature_c) * 0.8), 1)

    return {
        "location": location,
        "temperature_c": temperature_c,
        "humidity": humidity,
        "wind_speed_kmh": wind_speed_kmh,
        "rain_forecast": rain_forecast,
        "spray_status": spray_status,
        "spray_advisory": spray_advisory,
        "disease_risks": {
            "Powdery Mildew Risk": f"{powdery_mildew_risk}%",
            "Late / Early Blight Risk": f"{late_blight_risk}%"
        }
    }
