from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.seed_purchase_schema import (
    SeedPurchaseCreate,
    SeedPurchaseUpdate,
    SeedPurchaseResponse
)

from app.services.seed_purchase_service import (
    buy_seed,
    get_my_purchases,
    get_all_purchases,
    get_purchase_by_id,
    update_purchase_status,
    delete_purchase
)

router = APIRouter(
    prefix="/api/seed-purchase",
    tags=["Seed Purchase"]
)


@router.post(
    "/buy",
    response_model=SeedPurchaseResponse
)
def purchase_seed(
    purchase: SeedPurchaseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = buy_seed(
        db,
        purchase,
        current_user.id
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Seed not found"
        )

    if isinstance(result, dict):
        raise HTTPException(
            status_code=400,
            detail=result["error"]
        )

    return result


@router.get(
    "/my-purchases",
    response_model=list[SeedPurchaseResponse]
)
def my_purchases(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_my_purchases(
        db,
        current_user.id
    )


@router.get(
    "/all",
    response_model=list[SeedPurchaseResponse]
)
def all_purchases(
    db: Session = Depends(get_db)
):

    return get_all_purchases(db)


@router.get(
    "/{purchase_id}",
    response_model=SeedPurchaseResponse
)
def purchase_details(
    purchase_id: int,
    db: Session = Depends(get_db)
):

    purchase = get_purchase_by_id(
        db,
        purchase_id
    )

    if not purchase:
        raise HTTPException(
            status_code=404,
            detail="Purchase not found"
        )

    return purchase


@router.put(
    "/{purchase_id}",
    response_model=SeedPurchaseResponse
)
def update_status(
    purchase_id: int,
    purchase: SeedPurchaseUpdate,
    db: Session = Depends(get_db)
):

    updated = update_purchase_status(
        db,
        purchase_id,
        purchase
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Purchase not found"
        )

    return updated


@router.delete(
    "/{purchase_id}"
)
def remove_purchase(
    purchase_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_purchase(
        db,
        purchase_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Purchase not found"
        )

    return deleted