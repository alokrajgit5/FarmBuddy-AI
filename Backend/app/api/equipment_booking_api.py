from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.equipment_booking_schema import (
    EquipmentBookingCreate,
    EquipmentBookingUpdate,
    EquipmentBookingResponse
)

from app.services.equipment_booking_service import (
    create_booking,
    get_my_bookings,
    get_booking_by_id,
    update_booking_status,
    cancel_booking,
    get_all_bookings,
    get_owner_bookings,
    booking_history
)

router = APIRouter(
    prefix="/api/equipment-booking",
    tags=["Equipment Booking"]
)


@router.post(
    "/",
    response_model=EquipmentBookingResponse
)
def book_equipment(
    booking: EquipmentBookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = create_booking(
        db,
        booking,
        current_user.id
    )

    if isinstance(result, dict):
        raise HTTPException(
            status_code=400,
            detail=result["error"]
        )

    return result


@router.get(
    "/my-bookings",
    response_model=list[EquipmentBookingResponse]
)
def my_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_my_bookings(
        db,
        current_user.id
    )


@router.get(
    "/owner-bookings",
    response_model=list[EquipmentBookingResponse]
)
def owner_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_owner_bookings(
        db,
        current_user.id
    )


@router.get(
    "/history",
    response_model=list[EquipmentBookingResponse]
)
def my_booking_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return booking_history(
        db,
        current_user.id
    )


@router.get(
    "/",
    response_model=list[EquipmentBookingResponse]
)
def all_bookings(
    db: Session = Depends(get_db)
):

    return get_all_bookings(db)


@router.get(
    "/{booking_id}",
    response_model=EquipmentBookingResponse
)
def booking_details(
    booking_id: int,
    db: Session = Depends(get_db)
):

    booking = get_booking_by_id(
        db,
        booking_id
    )

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking


@router.put(
    "/{booking_id}",
    response_model=EquipmentBookingResponse
)
def change_booking_status(
    booking_id: int,
    booking: EquipmentBookingUpdate,
    db: Session = Depends(get_db)
):

    updated = update_booking_status(
        db,
        booking_id,
        booking
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return updated


@router.put(
    "/cancel/{booking_id}",
    response_model=EquipmentBookingResponse
)
def cancel_equipment_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):

    booking = cancel_booking(
        db,
        booking_id
    )

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking