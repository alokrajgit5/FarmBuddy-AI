from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.labor_schema import (
    LaborCreate,
    LaborUpdate,
    LaborResponse
)

from app.services.labor_service import (
    create_labor,
    get_all_labors,
    get_labor_by_id,
    update_labor,
    delete_labor
)

router = APIRouter(
    prefix="/api/labor",
    tags=["Labor Hiring"]
)


@router.post(
    "/",
    response_model=LaborResponse
)
def add_labor(
    labor: LaborCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_labor(
        db,
        labor,
        current_user.id
    )


@router.get(
    "/",
    response_model=list[LaborResponse]
)
def all_labors(
    db: Session = Depends(get_db)
):

    return get_all_labors(db)


@router.get(
    "/{labor_id}",
    response_model=LaborResponse
)
def single_labor(
    labor_id: int,
    db: Session = Depends(get_db)
):

    labor = get_labor_by_id(
        db,
        labor_id
    )

    if not labor:
        raise HTTPException(
            status_code=404,
            detail="Labor not found"
        )

    return labor


@router.put(
    "/{labor_id}",
    response_model=LaborResponse
)
def edit_labor(
    labor_id: int,
    labor: LaborUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    updated = update_labor(
        db,
        labor_id,
        labor
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Labor not found"
        )

    return updated


@router.delete(
    "/{labor_id}"
)
def remove_labor(
    labor_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    deleted = delete_labor(
        db,
        labor_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Labor not found"
        )

    return deleted