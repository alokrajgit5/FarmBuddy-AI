from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.dependencies.auth import get_current_user

from app.schemas.profile_schema import (
    ProfileCreate,
    ProfileResponse
)

from app.services.profile_service import (
    create_profile,
    get_profile,
    update_profile
)

router = APIRouter(
    prefix="/api/profile",
    tags=["Profile"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/create",
    response_model=ProfileResponse
)
def create_farmer_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    existing = get_profile(
        db,
        current_user.id
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Profile already exists"
        )

    return create_profile(
        db,
        profile,
        current_user.id
    )


@router.get(
    "/me",
    response_model=ProfileResponse
)
def my_profile(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    profile = get_profile(
        db,
        current_user.id
    )

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    return profile


@router.put(
    "/update",
    response_model=ProfileResponse
)
def edit_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    updated = update_profile(
        db,
        current_user.id,
        profile
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    return updated