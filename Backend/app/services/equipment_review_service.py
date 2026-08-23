from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.equipment import Equipment
from app.models.equipment_review import EquipmentReview

from app.schemas.equipment_review_schema import (
    EquipmentReviewCreate,
    EquipmentReviewUpdate
)


def add_review(
    db: Session,
    review: EquipmentReviewCreate,
    reviewer_id: int
):

    equipment = db.query(Equipment).filter(
        Equipment.id == review.equipment_id
    ).first()

    if not equipment:
        return {
            "error": "Equipment not found"
        }

    existing = db.query(
        EquipmentReview
    ).filter(

        EquipmentReview.equipment_id == review.equipment_id,

        EquipmentReview.reviewer_id == reviewer_id

    ).first()

    if existing:
        return {
            "error": "You have already reviewed this equipment"
        }

    new_review = EquipmentReview(

        equipment_id=review.equipment_id,

        reviewer_id=reviewer_id,

        rating=review.rating,

        review=review.review

    )

    db.add(new_review)

    db.commit()

    db.refresh(new_review)

    return new_review


def get_equipment_reviews(
    db: Session,
    equipment_id: int
):

    return db.query(
        EquipmentReview
    ).filter(

        EquipmentReview.equipment_id == equipment_id

    ).all()


def get_my_reviews(
    db: Session,
    reviewer_id: int
):

    return db.query(
        EquipmentReview
    ).filter(

        EquipmentReview.reviewer_id == reviewer_id

    ).all()


def get_review_by_id(
    db: Session,
    review_id: int
):

    return db.query(
        EquipmentReview
    ).filter(

        EquipmentReview.id == review_id

    ).first()


def update_review(
    db: Session,
    review_id: int,
    review: EquipmentReviewUpdate
):

    db_review = db.query(
        EquipmentReview
    ).filter(

        EquipmentReview.id == review_id

    ).first()

    if not db_review:
        return None

    db_review.rating = review.rating

    db_review.review = review.review

    db.commit()

    db.refresh(db_review)

    return db_review


def delete_review(
    db: Session,
    review_id: int
):

    db_review = db.query(
        EquipmentReview
    ).filter(

        EquipmentReview.id == review_id

    ).first()

    if not db_review:
        return None

    db.delete(db_review)

    db.commit()

    return {
        "message": "Review deleted successfully"
    }


def get_average_rating(
    db: Session,
    equipment_id: int
):

    average = db.query(

        func.avg(
            EquipmentReview.rating
        )

    ).filter(

        EquipmentReview.equipment_id == equipment_id

    ).scalar()

    return round(
        average,
        1
    ) if average else 0


def get_rating_summary(
    db: Session,
    equipment_id: int
):

    return {

        "5_star": db.query(EquipmentReview).filter(
            EquipmentReview.equipment_id == equipment_id,
            EquipmentReview.rating == 5
        ).count(),

        "4_star": db.query(EquipmentReview).filter(
            EquipmentReview.equipment_id == equipment_id,
            EquipmentReview.rating == 4
        ).count(),

        "3_star": db.query(EquipmentReview).filter(
            EquipmentReview.equipment_id == equipment_id,
            EquipmentReview.rating == 3
        ).count(),

        "2_star": db.query(EquipmentReview).filter(
            EquipmentReview.equipment_id == equipment_id,
            EquipmentReview.rating == 2
        ).count(),

        "1_star": db.query(EquipmentReview).filter(
            EquipmentReview.equipment_id == equipment_id,
            EquipmentReview.rating == 1
        ).count()

    }


def get_top_rated_equipment(
    db: Session
):

    return (

        db.query(

            Equipment.id,

            Equipment.equipment_name,

            func.avg(
                EquipmentReview.rating
            ).label(
                "average_rating"
            )

        )

        .join(

            EquipmentReview,

            Equipment.id ==
            EquipmentReview.equipment_id

        )

        .group_by(

            Equipment.id,

            Equipment.equipment_name

        )

        .order_by(

            func.avg(
                EquipmentReview.rating
            ).desc()

        )

        .all()

    )