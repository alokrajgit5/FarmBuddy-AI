from fastapi import APIRouter

from app.schemas.scheme_schema import (
    SchemeRequest,
    SchemeResponse
)

from app.services.scheme_service import (
    recommend_scheme
)

router = APIRouter(
    prefix="/api/schemes",
    tags=["Government Schemes"]
)


@router.post(
    "/recommend",
    response_model=SchemeResponse
)
def recommend(
    data: SchemeRequest
):

    return recommend_scheme(data)