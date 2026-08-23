from fastapi import APIRouter

from app.schemas.fertilizer_schema import (
    FertilizerRequest,
    FertilizerResponse
)

from app.services.fertilizer_service import (
    recommend_fertilizer
)

router = APIRouter(
    prefix="/api/fertilizer",
    tags=["Fertilizer"]
)


@router.post(
    "/recommend",
    response_model=FertilizerResponse
)
def recommend(
    data: FertilizerRequest
):

    return recommend_fertilizer(data)