from datetime import timedelta

from sqlalchemy.orm import Session

from app.models.equipment import Equipment
from app.models.equipment_booking import EquipmentBooking

from app.schemas.equipment_booking_schema import (
    EquipmentBookingCreate,
    EquipmentBookingUpdate
)


def create_booking(
    db: Session,
    booking: EquipmentBookingCreate,
    renter_id: int
):

    equipment = db.query(Equipment).filter(
        Equipment.id == booking.equipment_id
    ).first()

    if not equipment:
        return {
            "error": "Equipment not found"
        }

    if equipment.availability != "Available":
        return {
            "error": "Equipment is not available"
        }

    # Check Date
    if booking.end_date < booking.start_date:
        return {
            "error": "Invalid booking dates"
        }

    # Check Existing Booking
    existing = db.query(
        EquipmentBooking
    ).filter(

        EquipmentBooking.equipment_id == booking.equipment_id,

        EquipmentBooking.status.in_(
            [
                "Pending",
                "Approved",
                "Running"
            ]
        )

    ).all()

    for item in existing:

        if not (

            booking.end_date < item.start_date

            or

            booking.start_date > item.end_date

        ):

            return {
                "error": "Equipment already booked for selected dates"
            }

    total_days = (
        booking.end_date -
        booking.start_date
    ).days + 1

    total_amount = (
        total_days *
        equipment.price_per_day
    )

    new_booking = EquipmentBooking(

        equipment_id=booking.equipment_id,

        renter_id=renter_id,

        start_date=booking.start_date,

        end_date=booking.end_date,

        total_days=total_days,

        total_amount=total_amount,

        status="Pending"

    )

    db.add(new_booking)

    db.commit()

    db.refresh(new_booking)

    return new_booking


def get_my_bookings(
    db: Session,
    renter_id: int
):

    return db.query(
        EquipmentBooking
    ).filter(

        EquipmentBooking.renter_id == renter_id

    ).all()


def get_booking_by_id(
    db: Session,
    booking_id: int
):

    return db.query(
        EquipmentBooking
    ).filter(

        EquipmentBooking.id == booking_id

    ).first()


def update_booking_status(
    db: Session,
    booking_id: int,
    booking: EquipmentBookingUpdate
):

    db_booking = db.query(
        EquipmentBooking
    ).filter(

        EquipmentBooking.id == booking_id

    ).first()

    if not db_booking:
        return None

    db_booking.status = booking.status

    db.commit()

    db.refresh(db_booking)

    return db_booking


def cancel_booking(
    db: Session,
    booking_id: int
):

    booking = db.query(
        EquipmentBooking
    ).filter(

        EquipmentBooking.id == booking_id

    ).first()

    if not booking:
        return None

    booking.status = "Cancelled"

    db.commit()

    db.refresh(booking)

    return booking


def get_all_bookings(
    db: Session
):

    return db.query(
        EquipmentBooking
    ).all()


def get_owner_bookings(
    db: Session,
    owner_id: int
):

    return (

        db.query(
            EquipmentBooking
        )

        .join(
            Equipment,
            Equipment.id ==
            EquipmentBooking.equipment_id
        )

        .filter(
            Equipment.owner_id == owner_id
        )

        .all()

    )


def booking_history(
    db: Session,
    renter_id: int
):

    return db.query(
        EquipmentBooking
    ).filter(

        EquipmentBooking.renter_id == renter_id

    ).order_by(

        EquipmentBooking.id.desc()

    ).all()