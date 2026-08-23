from sqlalchemy.orm import Session

from app.models.crop import Crop
from app.schemas.crop_schema import CropCreate


def create_crop(
    db: Session,
    crop: CropCreate,
    user_id: int
):

    new_crop = Crop(
        crop_name=crop.crop_name,
        season=crop.season,
        area=crop.area,
        irrigation=crop.irrigation,
        fertilizer=crop.fertilizer,
        expected_yield=crop.expected_yield,
        owner_id=user_id
    )

    db.add(new_crop)
    db.commit()
    db.refresh(new_crop)

    return new_crop


def get_my_crops(
    db: Session,
    user_id: int
):

    return db.query(Crop).filter(
        Crop.owner_id == user_id
    ).all()


def get_crop_by_id(
    db: Session,
    crop_id: int,
    user_id: int
):

    return db.query(Crop).filter(
        Crop.id == crop_id,
        Crop.owner_id == user_id
    ).first()


def update_crop(
    db: Session,
    crop_id: int,
    crop: CropCreate,
    user_id: int
):

    existing = get_crop_by_id(
        db,
        crop_id,
        user_id
    )

    if not existing:
        return None

    existing.crop_name = crop.crop_name
    existing.season = crop.season
    existing.area = crop.area
    existing.irrigation = crop.irrigation
    existing.fertilizer = crop.fertilizer
    existing.expected_yield = crop.expected_yield

    db.commit()
    db.refresh(existing)

    return existing


def delete_crop(
    db: Session,
    crop_id: int,
    user_id: int
):

    crop = get_crop_by_id(
        db,
        crop_id,
        user_id
    )

    if not crop:
        return None

    db.delete(crop)
    db.commit()

    return True