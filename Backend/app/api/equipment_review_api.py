from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.equipment_review_schema import (
    EquipmentReviewCreate,
    EquipmentReviewUpdate,
    EquipmentReviewResponse
)

from app.services.equipment_review_service import (
    add_review,
    get_equipment_reviews,
    get_my_reviews,
    get_review_by_id,
    update_review,
    delete_review,
    get_average_rating,
    get_rating_summary,
    get_top_rated_equipment
)

router = APIRouter(
    prefix="/api/equipment-review",
    tags=["Equipment Review"]
)


@router.post(
    "/",
    response_model=EquipmentReviewResponse
)
def create_review(
    review: EquipmentReviewCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = add_review(
        db,
        review,
        current_user.id
    )

    if isinstance(result, dict):
        raise HTTPException(
            status_code=400,
            detail=result["error"]
        )

    return result


@router.get(
    "/my-reviews",
    response_model=list[EquipmentReviewResponse]
)
def my_reviews(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_my_reviews(
        db,
        current_user.id
    )


@router.get(
    "/equipment/{equipment_id}",
    response_model=list[EquipmentReviewResponse]
)
def equipment_reviews(
    equipment_id: int,
    db: Session = Depends(get_db)
):

    return get_equipment_reviews(
        db,
        equipment_id
    )


@router.get(
    "/{review_id}",
    response_model=EquipmentReviewResponse
)
def review_details(
    review_id: int,
    db: Session = Depends(get_db)
):

    review = get_review_by_id(
        db,
        review_id
    )

    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return review


@router.put(
    "/{review_id}",
    response_model=EquipmentReviewResponse
)
def edit_review(
    review_id: int,
    review: EquipmentReviewUpdate,
    db: Session = Depends(get_db)
):

    updated = update_review(
        db,
        review_id,
        review
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return updated


@router.delete(
    "/{review_id}"
)
def remove_review(
    review_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_review(
        db,
        review_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return deleted


@router.get(
    "/average/{equipment_id}"
)
def average_rating(
    equipment_id: int,
    db: Session = Depends(get_db)
):

    return {
        "equipment_id": equipment_id,
        "average_rating": get_average_rating(
            db,
            equipment_id
        )
    }


@router.get(
    "/summary/{equipment_id}"
)
def rating_summary(
    equipment_id: int,
    db: Session = Depends(get_db)
):

    return get_rating_summary(
        db,
        equipment_id
    )


@router.get(
    "/top-rated"
)
def top_rated_equipment(
    db: Session = Depends(get_db)
):

    return get_top_rated_equipment(
        db
    )