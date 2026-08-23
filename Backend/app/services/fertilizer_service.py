from app.schemas.fertilizer_schema import (
    FertilizerRequest
)


def recommend_fertilizer(data: FertilizerRequest):

    crop = data.crop.lower()

    n = data.nitrogen
    p = data.phosphorus
    k = data.potassium

    recommendation = {}

    # Rice
    if crop == "rice":

        if n < 50:
            recommendation = {
                "fertilizer": "Urea",
                "quantity": "45 kg/acre",
                "application_method": "Broadcast",
                "instructions": "Apply after irrigation."
            }

        elif p < 40:
            recommendation = {
                "fertilizer": "DAP",
                "quantity": "40 kg/acre",
                "application_method": "Basal Application",
                "instructions": "Mix with soil before sowing."
            }

        elif k < 40:
            recommendation = {
                "fertilizer": "MOP",
                "quantity": "20 kg/acre",
                "application_method": "Top Dressing",
                "instructions": "Apply during vegetative stage."
            }

        else:
            recommendation = {
                "fertilizer": "NPK 19:19:19",
                "quantity": "25 kg/acre",
                "application_method": "Foliar Spray",
                "instructions": "Spray every 20 days."
            }

    # Wheat
    elif crop == "wheat":

        recommendation = {
            "fertilizer": "DAP",
            "quantity": "50 kg/acre",
            "application_method": "Basal Application",
            "instructions": "Apply during field preparation."
        }

    # Cotton
    elif crop == "cotton":

        recommendation = {
            "fertilizer": "Potash",
            "quantity": "25 kg/acre",
            "application_method": "Soil Application",
            "instructions": "Apply before flowering."
        }

    # Tomato
    elif crop == "tomato":

        recommendation = {
            "fertilizer": "Organic Compost",
            "quantity": "2 Ton/acre",
            "application_method": "Mix with Soil",
            "instructions": "Apply before transplanting."
        }

    # Potato
    elif crop == "potato":

        recommendation = {
            "fertilizer": "NPK 10:26:26",
            "quantity": "50 kg/acre",
            "application_method": "Basal Application",
            "instructions": "Apply before planting."
        }

    # Default
    else:

        recommendation = {
            "fertilizer": "NPK 19:19:19",
            "quantity": "25 kg/acre",
            "application_method": "Soil Application",
            "instructions": "Apply according to soil test."
        }

    return recommendation