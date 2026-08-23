from app.schemas.recommendation_schema import RecommendationRequest


def recommend_crop(data: RecommendationRequest):

    recommendations = []

    # Rice
    if (
        data.temperature >= 25
        and data.humidity >= 70
        and data.moisture >= 60
        and data.nitrogen >= 80
    ):
        recommendations.append({
            "crop": "Rice",
            "confidence": 95,
            "season": "Kharif",
            "fertilizer": "Urea + DAP"
        })

    # Wheat
    if (
        15 <= data.temperature <= 25
        and data.humidity <= 60
        and data.nitrogen >= 60
        and data.phosphorus >= 40
    ):
        recommendations.append({
            "crop": "Wheat",
            "confidence": 90,
            "season": "Rabi",
            "fertilizer": "DAP + Potash"
        })

    # Maize
    if (
        20 <= data.temperature <= 30
        and data.potassium >= 50
        and data.nitrogen >= 50
    ):
        recommendations.append({
            "crop": "Maize",
            "confidence": 88,
            "season": "Kharif",
            "fertilizer": "NPK 20:20:20"
        })

    # Cotton
    if (
        data.temperature >= 30
        and data.humidity <= 50
        and data.ph > 7
    ):
        recommendations.append({
            "crop": "Cotton",
            "confidence": 86,
            "season": "Kharif",
            "fertilizer": "Potash"
        })

    # Potato
    if (
        data.temperature <= 20
        and data.ph < 6.5
    ):
        recommendations.append({
            "crop": "Potato",
            "confidence": 85,
            "season": "Rabi",
            "fertilizer": "DAP"
        })

    # Groundnut
    if not recommendations:
        recommendations.append({
            "crop": "Groundnut",
            "confidence": 75,
            "season": "Kharif",
            "fertilizer": "NPK"
        })

    recommendations.sort(
        key=lambda x: x["confidence"],
        reverse=True
    )

    return {
        "recommendations": recommendations[:3]
    }