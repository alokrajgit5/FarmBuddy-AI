from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User

from app.schemas.labor_booking_schema import (
    LaborBookingCreate,
    LaborBookingResponse,
    LaborBookingUpdate
)

from app.services.labor_booking_service import (
    create_booking,
    get_my_bookings,
    get_all_bookings,
    get_booking_by_id,
    update_booking_status,
    delete_booking
)

router = APIRouter(
    prefix="/api/labor-booking",
    tags=["Labor Booking"]
)


@router.post(
    "/book",
    response_model=LaborBookingResponse
)
def book_labor(
    booking: LaborBookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_booking = create_booking(
        db,
        booking,
        current_user.id
    )

    if not new_booking:
        raise HTTPException(
            status_code=404,
            detail="Labor not found"
        )

    return new_booking


@router.get(
    "/my-bookings",
    response_model=list[LaborBookingResponse]
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
    "/all",
    response_model=list[LaborBookingResponse]
)
def all_bookings(
    db: Session = Depends(get_db)
):

    return get_all_bookings(db)


@router.get(
    "/{booking_id}",
    response_model=LaborBookingResponse
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
    response_model=LaborBookingResponse
)
def update_status(
    booking_id: int,
    booking: LaborBookingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
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


@router.delete(
    "/{booking_id}"
)
def remove_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    deleted = delete_booking(
        db,
        booking_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return deleted