from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.equipment_schema import (
    EquipmentCreate,
    EquipmentUpdate,
    EquipmentResponse
)

from app.services.equipment_service import (
    create_equipment,
    get_all_equipment,
    get_equipment_by_id,
    update_equipment,
    delete_equipment,
    get_equipment_by_category,
    get_equipment_by_location,
    get_available_equipment,
    get_my_equipment
)

router = APIRouter(
    prefix="/api/equipment",
    tags=["Equipment"]
)


@router.post(
    "/",
    response_model=EquipmentResponse
)
def add_equipment(
    equipment: EquipmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_equipment(
        db,
        equipment,
        current_user.id
    )


@router.get(
    "/",
    response_model=list[EquipmentResponse]
)
def all_equipment(
    db: Session = Depends(get_db)
):

    return get_all_equipment(db)


@router.get(
    "/my-equipment",
    response_model=list[EquipmentResponse]
)
def my_equipment(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_my_equipment(
        db,
        current_user.id
    )


@router.get(
    "/available",
    response_model=list[EquipmentResponse]
)
def available_equipment(
    db: Session = Depends(get_db)
):

    return get_available_equipment(db)


@router.get(
    "/category/{category}",
    response_model=list[EquipmentResponse]
)
def equipment_category(
    category: str,
    db: Session = Depends(get_db)
):

    return get_equipment_by_category(
        db,
        category
    )


@router.get(
    "/location/{location}",
    response_model=list[EquipmentResponse]
)
def equipment_location(
    location: str,
    db: Session = Depends(get_db)
):

    return get_equipment_by_location(
        db,
        location
    )


@router.get(
    "/{equipment_id}",
    response_model=EquipmentResponse
)
def equipment_details(
    equipment_id: int,
    db: Session = Depends(get_db)
):

    equipment = get_equipment_by_id(
        db,
        equipment_id
    )

    if not equipment:
        raise HTTPException(
            status_code=404,
            detail="Equipment not found"
        )

    return equipment


@router.put(
    "/{equipment_id}",
    response_model=EquipmentResponse
)
def edit_equipment(
    equipment_id: int,
    equipment: EquipmentUpdate,
    db: Session = Depends(get_db)
):

    updated = update_equipment(
        db,
        equipment_id,
        equipment
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Equipment not found"
        )

    return updated


@router.delete(
    "/{equipment_id}"
)
def remove_equipment(
    equipment_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_equipment(
        db,
        equipment_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Equipment not found"
        )

    return deleted