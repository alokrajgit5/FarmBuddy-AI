from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.dependencies.auth import get_current_user

from app.schemas.tractor_booking_schema import (
    TractorBookingCreate,
    TractorBookingResponse
)

from app.services.tractor_booking_service import (
    create_booking,
    get_my_bookings,
    get_tractor_bookings,
    update_booking_status,
    delete_booking
)

router = APIRouter(
    prefix="/api/tractor-booking",
    tags=["Tractor Booking"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/book",
    response_model=TractorBookingResponse
)
def book_tractor(
    booking: TractorBookingCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    new_booking = create_booking(
        db,
        booking,
        current_user.id
    )

    if new_booking is None:
        raise HTTPException(
            status_code=404,
            detail="Tractor not found"
        )

    return new_booking


@router.get(
    "/my-bookings",
    response_model=list[TractorBookingResponse]
)
def my_bookings(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_my_bookings(
        db,
        current_user.id
    )


@router.get(
    "/owner-bookings",
    response_model=list[TractorBookingResponse]
)
def owner_bookings(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_tractor_bookings(
        db,
        current_user.id
    )


@router.put(
    "/approve/{booking_id}",
    response_model=TractorBookingResponse
)
def approve_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    booking = update_booking_status(
        db,
        booking_id,
        "Approved"
    )

    if booking is None:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking


@router.put(
    "/reject/{booking_id}",
    response_model=TractorBookingResponse
)
def reject_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    booking = update_booking_status(
        db,
        booking_id,
        "Rejected"
    )

    if booking is None:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking


@router.delete(
    "/cancel/{booking_id}"
)
def cancel_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    deleted = delete_booking(
        db,
        booking_id,
        current_user.id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return {
        "message": "Booking cancelled successfully."
    }