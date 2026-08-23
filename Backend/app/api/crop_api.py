from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.dependencies.auth import get_current_user

from app.schemas.crop_schema import (
    CropCreate,
    CropResponse
)

from app.services.crop_service import (
    create_crop,
    get_my_crops,
    update_crop,
    delete_crop,
    get_crop_by_id
)

router = APIRouter(
    prefix="/api/crops",
    tags=["Crops"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/create",
    response_model=CropResponse
)
def add_crop(
    crop: CropCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_crop(
        db,
        crop,
        current_user.id
    )


@router.get(
    "/my",
    response_model=list[CropResponse]
)
def my_crops(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_my_crops(
        db,
        current_user.id
    )


@router.put(
    "/update/{crop_id}",
    response_model=CropResponse
)
def edit_crop(
    crop_id: int,
    crop: CropCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    updated = update_crop(
        db,
        crop_id,
        crop,
        current_user.id
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )

    return updated


@router.delete("/delete/{crop_id}")
def remove_crop(
    crop_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    deleted = delete_crop(
        db,
        crop_id,
        current_user.id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )

    return {
        "message": "Crop deleted successfully"
    }


@router.get(
    "/{crop_id}",
    response_model=CropResponse
)
def get_crop(
    crop_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    crop = get_crop_by_id(
        db,
        crop_id,
        current_user.id
    )

    if not crop:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )

    return crop