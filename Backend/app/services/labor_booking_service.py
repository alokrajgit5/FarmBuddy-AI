from sqlalchemy.orm import Session

from app.models.labor import Labor
from app.models.labor_booking import LaborBooking

from app.schemas.labor_booking_schema import (
    LaborBookingCreate,
    LaborBookingUpdate
)


def create_booking(
    db: Session,
    booking: LaborBookingCreate,
    farmer_id: int
):

    labor = db.query(Labor).filter(
        Labor.id == booking.labor_id
    ).first()

    if labor is None:
        return None

    total_amount = (
        labor.daily_wage *
        booking.working_days
    )

    new_booking = LaborBooking(

        farmer_id=farmer_id,

        labor_id=booking.labor_id,

        booking_date=booking.booking_date,

        working_days=booking.working_days,

        total_amount=total_amount,

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
        LaborBooking
    ).filter(
        LaborBooking.farmer_id == farmer_id
    ).all()


def get_all_bookings(
    db: Session
):

    return db.query(
        LaborBooking
    ).all()


def get_booking_by_id(
    db: Session,
    booking_id: int
):

    return db.query(
        LaborBooking
    ).filter(
        LaborBooking.id == booking_id
    ).first()


def update_booking_status(
    db: Session,
    booking_id: int,
    booking: LaborBookingUpdate
):

    db_booking = db.query(
        LaborBooking
    ).filter(
        LaborBooking.id == booking_id
    ).first()

    if not db_booking:
        return None

    db_booking.status = booking.status

    db.commit()

    db.refresh(db_booking)

    return db_booking


def delete_booking(
    db: Session,
    booking_id: int
):

    db_booking = db.query(
        LaborBooking
    ).filter(
        LaborBooking.id == booking_id
    ).first()

    if not db_booking:
        return None

    db.delete(db_booking)

    db.commit()

    return {
        "message": "Booking deleted successfully"
    }