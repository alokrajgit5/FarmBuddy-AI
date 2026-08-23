from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.payment_schema import (
    PaymentCreate,
    PaymentUpdate,
    PaymentResponse
)

from app.services.payment_service import (
    create_payment,
    get_my_payments,
    get_payment_by_id,
    update_payment,
    delete_payment,
    payment_history,
    get_total_revenue,
    get_payment_statistics
)

router = APIRouter(
    prefix="/api/payments",
    tags=["Payments"]
)


@router.post(
    "/",
    response_model=PaymentResponse
)
def make_payment(
    payment: PaymentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = create_payment(
        db,
        payment,
        current_user.id
    )

    if isinstance(result, dict):

        raise HTTPException(
            status_code=400,
            detail=result["error"]
        )

    return result


@router.get(
    "/",
    response_model=list[PaymentResponse]
)
def my_payments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_my_payments(
        db,
        current_user.id
    )


@router.get(
    "/history",
    response_model=list[PaymentResponse]
)
def my_payment_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return payment_history(
        db,
        current_user.id
    )


@router.get("/statistics")
def payment_statistics(
    db: Session = Depends(get_db)
):

    return get_payment_statistics(db)


@router.get("/revenue")
def total_revenue(
    db: Session = Depends(get_db)
):

    return {
        "total_revenue": get_total_revenue(db)
    }


@router.get(
    "/{payment_id}",
    response_model=PaymentResponse
)
def payment_details(
    payment_id: int,
    db: Session = Depends(get_db)
):

    payment = get_payment_by_id(
        db,
        payment_id
    )

    if not payment:

        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return payment


@router.put(
    "/{payment_id}",
    response_model=PaymentResponse
)
def edit_payment(
    payment_id: int,
    payment: PaymentUpdate,
    db: Session = Depends(get_db)
):

    updated = update_payment(
        db,
        payment_id,
        payment
    )

    if not updated:

        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return updated


@router.delete(
    "/{payment_id}"
)
def remove_payment(
    payment_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_payment(
        db,
        payment_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return deleted