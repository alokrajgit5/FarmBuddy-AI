from fastapi import APIRouter

from app.schemas.crop_recommendation_schema import (
    CropRecommendationRequest,
    CropRecommendationResponse
)

from app.services.crop_recommendation_service import (
    recommend_crop
)

router = APIRouter(
    prefix="/api/crop-recommendation",
    tags=["Crop Recommendation"]
)


@router.post(
    "/recommend",
    response_model=CropRecommendationResponse
)
def recommend(
    data: CropRecommendationRequest
):

    return recommend_crop(data)