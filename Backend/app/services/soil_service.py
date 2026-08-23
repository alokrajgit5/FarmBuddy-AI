from sqlalchemy.orm import Session

from app.models.soil import Soil
from app.schemas.soil_schema import SoilCreate


def create_soil(
    db: Session,
    soil: SoilCreate,
    user_id: int
):
    new_soil = Soil(
        user_id=user_id,
        nitrogen=soil.nitrogen,
        phosphorus=soil.phosphorus,
        potassium=soil.potassium,
        ph=soil.ph,
        moisture=soil.moisture
    )

    db.add(new_soil)
    db.commit()
    db.refresh(new_soil)

    return new_soil


def get_my_soil(
    db: Session,
    user_id: int
):
    return db.query(Soil).filter(
        Soil.user_id == user_id
    ).all()
def analyze_soil(
    nitrogen: float,
    phosphorus: float,
    potassium: float,
    ph: float,
    moisture: float
):

    recommendations = []

    if nitrogen < 50:
        recommendations.append(
            "Nitrogen is low. Use Nitrogen fertilizer."
        )

    if phosphorus < 30:
        recommendations.append(
            "Phosphorus is low. Add DAP fertilizer."
        )

    if potassium < 40:
        recommendations.append(
            "Potassium is low. Use Potash fertilizer."
        )

    if ph < 6:
        recommendations.append(
            "Soil is acidic. Add Lime."
        )

    elif ph > 8:
        recommendations.append(
            "Soil is alkaline. Add Gypsum."
        )

    if moisture < 30:
        recommendations.append(
            "Increase irrigation."
        )

    if not recommendations:
        recommendations.append(
            "Soil is healthy. Suitable for most crops."
        )

    return "\n".join(recommendations)