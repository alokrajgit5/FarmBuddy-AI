from fastapi import APIRouter

from app.schemas.recommendation_schema import (
    RecommendationRequest,
    RecommendationResponse
)

from app.services.recommendation_service import (
    recommend_crop
)

router = APIRouter(
    prefix="/api/recommendation",
    tags=["Crop Recommendation"]
)


@router.post(
    "/crop",
    response_model=RecommendationResponse
)
def crop_recommendation(
    data: RecommendationRequest
):

    result = recommend_crop(data)

    return result