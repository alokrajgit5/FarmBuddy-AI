from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.payment import Payment
from app.models.equipment_booking import EquipmentBooking

from app.schemas.payment_schema import (
    PaymentCreate,
    PaymentUpdate
)


def create_payment(
    db: Session,
    payment: PaymentCreate,
    user_id: int
):

    booking = db.query(
        EquipmentBooking
    ).filter(

        EquipmentBooking.id == payment.booking_id

    ).first()

    if not booking:

        return {
            "error": "Booking not found"
        }

    existing = db.query(
        Payment
    ).filter(

        Payment.booking_id == payment.booking_id,

        Payment.payment_status == "Success"

    ).first()

    if existing:

        return {
            "error": "Payment already completed"
        }

    new_payment = Payment(

        user_id=user_id,

        booking_id=payment.booking_id,

        amount=booking.total_amount,

        payment_method=payment.payment_method,

        payment_status="Pending"

    )

    db.add(new_payment)

    db.commit()

    db.refresh(new_payment)

    return new_payment


def get_my_payments(
    db: Session,
    user_id: int
):

    return db.query(
        Payment
    ).filter(

        Payment.user_id == user_id

    ).all()


def get_payment_by_id(
    db: Session,
    payment_id: int
):

    return db.query(
        Payment
    ).filter(

        Payment.id == payment_id

    ).first()


def update_payment(
    db: Session,
    payment_id: int,
    payment: PaymentUpdate
):

    db_payment = db.query(
        Payment
    ).filter(

        Payment.id == payment_id

    ).first()

    if not db_payment:

        return None

    db_payment.payment_status = payment.payment_status

    db_payment.transaction_id = payment.transaction_id

    db.commit()

    db.refresh(db_payment)

    return db_payment


def delete_payment(
    db: Session,
    payment_id: int
):

    db_payment = db.query(
        Payment
    ).filter(

        Payment.id == payment_id

    ).first()

    if not db_payment:

        return None

    db.delete(db_payment)

    db.commit()

    return {
        "message": "Payment deleted successfully"
    }


def payment_history(
    db: Session,
    user_id: int
):

    return db.query(
        Payment
    ).filter(

        Payment.user_id == user_id

    ).order_by(

        Payment.id.desc()

    ).all()


def get_total_revenue(
    db: Session
):

    revenue = db.query(

        func.sum(
            Payment.amount
        )

    ).filter(

        Payment.payment_status == "Success"

    ).scalar()

    return revenue or 0


def get_payment_statistics(
    db: Session
):

    return {

        "total_payments": db.query(
            Payment
        ).count(),

        "successful_payments": db.query(
            Payment
        ).filter(
            Payment.payment_status == "Success"
        ).count(),

        "pending_payments": db.query(
            Payment
        ).filter(
            Payment.payment_status == "Pending"
        ).count(),

        "failed_payments": db.query(
            Payment
        ).filter(
            Payment.payment_status == "Failed"
        ).count(),

        "refunded_payments": db.query(
            Payment
        ).filter(
            Payment.payment_status == "Refunded"
        ).count(),

        "total_revenue": get_total_revenue(db)

    }