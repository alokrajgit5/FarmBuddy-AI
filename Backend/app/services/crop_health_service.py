from random import randint, choice


def calculate_crop_health(total_crops: int):

    if total_crops <= 0:

        return {
            "health_score": 0,
            "health_status": "No Crops",
            "disease_risk": "Unknown",
            "recommendation": "Add crops to start monitoring."
        }

    score = randint(78, 99)

    if score >= 95:
        status = "Excellent"

    elif score >= 90:
        status = "Very Good"

    elif score >= 80:
        status = "Good"

    elif score >= 70:
        status = "Average"

    else:
        status = "Critical"

    disease = choice([
        "Low",
        "Low",
        "Low",
        "Medium",
        "High"
    ])

    recommendation = choice([
        "Maintain proper irrigation.",
        "Monitor leaves for diseases.",
        "Apply organic fertilizer.",
        "Increase soil moisture.",
        "Crop condition is excellent."
    ])

    return {
        "health_score": score,
        "health_status": status,
        "disease_risk": disease,
        "recommendation": recommendation
    }