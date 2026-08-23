from sqlalchemy.orm import Session

from app.models.tractor_booking import TractorBooking
from app.models.tractor import Tractor

from app.schemas.tractor_booking_schema import (
    TractorBookingCreate
)


def create_booking(
    db: Session,
    booking: TractorBookingCreate,
    farmer_id: int
):

    tractor = db.query(Tractor).filter(
        Tractor.id == booking.tractor_id
    ).first()

    if tractor is None:
        return None

    new_booking = TractorBooking(

        tractor_id=booking.tractor_id,

        farmer_id=farmer_id,

        booking_date=booking.booking_date,

        total_days=booking.total_days,

        message=booking.message,

        status="Pending"

    )

    db.add(new_booking)

    db.commit()

    db.refresh(new_booking)

    return new_booking


def get_my_bookings(
    db: Session,
    farmer_id: int
):

    return db.query(
        TractorBooking
    ).filter(
        TractorBooking.farmer_id == farmer_id
    ).all()


def get_tractor_bookings(
    db: Session,
    owner_id: int
):

    return db.query(
        TractorBooking
    ).join(
        Tractor
    ).filter(
        Tractor.owner_id == owner_id
    ).all()


def update_booking_status(
    db: Session,
    booking_id: int,
    status: str
):

    booking = db.query(
        TractorBooking
    ).filter(
        TractorBooking.id == booking_id
    ).first()

    if booking is None:
        return None

    booking.status = status

    db.commit()

    db.refresh(booking)

    return booking


def delete_booking(
    db: Session,
    booking_id: int,
    farmer_id: int
):

    booking = db.query(
        TractorBooking
    ).filter(
        TractorBooking.id == booking_id,
        TractorBooking.farmer_id == farmer_id
    ).first()

    if booking is None:
        return False

    db.delete(booking)

    db.commit()

    return True