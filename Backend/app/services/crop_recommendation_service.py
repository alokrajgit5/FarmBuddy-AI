from app.schemas.crop_recommendation_schema import (
    CropRecommendationRequest
)


def recommend_crop(data: CropRecommendationRequest):

    recommendations = []

    # Rice Conditions
    if (
        data.rainfall >= 200
        and data.humidity >= 80
    ):

        recommendations.append({
            "crop": "Rice",
            "suitability": "96%",
            "duration": "120 Days",
            "expected_yield": "25-30 Quintal/Acre",
            "advantages": [
                "High market demand",
                "Suitable for high rainfall",
                "Stable production"
            ]
        })

    # Wheat Conditions
    if (
        15 <= data.temperature <= 25
    ):

        recommendations.append({
            "crop": "Wheat",
            "suitability": "94%",
            "duration": "110 Days",
            "expected_yield": "20-25 Quintal/Acre",
            "advantages": [
                "Easy cultivation",
                "Good profit",
                "High demand"
            ]
        })

    # Cotton
    if (
        data.temperature >= 25
        and data.potassium >= 40
    ):

        recommendations.append({
            "crop": "Cotton",
            "suitability": "92%",
            "duration": "180 Days",
            "expected_yield": "8-12 Quintal/Acre",
            "advantages": [
                "Good export value",
                "High income",
                "Suitable for warm climate"
            ]
        })

    # Tomato
    if (
        6 <= data.ph <= 7
    ):

        recommendations.append({
            "crop": "Tomato",
            "suitability": "90%",
            "duration": "90 Days",
            "expected_yield": "200 Quintal/Acre",
            "advantages": [
                "Fast harvest",
                "High market value",
                "Good profit"
            ]
        })

    # Potato
    if (
        data.humidity >= 60
    ):

        recommendations.append({
            "crop": "Potato",
            "suitability": "89%",
            "duration": "100 Days",
            "expected_yield": "90 Quintal/Acre",
            "advantages": [
                "Good storage life",
                "Regular demand",
                "High production"
            ]
        })

    # Default
    if len(recommendations) == 0:

        recommendations.append({
            "crop": "Groundnut",
            "suitability": "80%",
            "duration": "110 Days",
            "expected_yield": "12 Quintal/Acre",
            "advantages": [
                "Low water requirement",
                "Suitable for dry climate",
                "Easy cultivation"
            ]
        })

    return {
        "recommendations": recommendations[:3]
    }