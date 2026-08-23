from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.dependencies.auth import get_current_user
from app.schemas.soil_schema import (
    SoilCreate,
    SoilResponse,
    SoilRecommendation
)
from app.services.soil_service import (
    create_soil,
    get_my_soil,
    analyze_soil
)

from app.schemas.soil_schema import (
    SoilCreate,
    SoilResponse
)

from app.services.soil_service import (
    create_soil,
    get_my_soil
)

router = APIRouter(
    prefix="/api/soil",
    tags=["Soil"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/create",
    response_model=SoilResponse
)
def add_soil(
    soil: SoilCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_soil(
        db,
        soil,
        current_user.id
    )


@router.get(
    "/my",
    response_model=list[SoilResponse]
)
def my_soil(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_my_soil(
        db,
        current_user.id
    )
@router.post(
    "/analyze",
    response_model=SoilRecommendation
)
def soil_analysis(
    soil: SoilCreate
):

    result = analyze_soil(
        soil.nitrogen,
        soil.phosphorus,
        soil.potassium,
        soil.ph,
        soil.moisture
    )

    return {
        "recommendation": result
    }