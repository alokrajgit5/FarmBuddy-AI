from sqlalchemy.orm import Session

from app.models.seed import Seed
from app.models.seed_purchase import SeedPurchase

from app.schemas.seed_purchase_schema import (
    SeedPurchaseCreate,
    SeedPurchaseUpdate
)


def buy_seed(
    db: Session,
    purchase: SeedPurchaseCreate,
    buyer_id: int
):

    seed = db.query(Seed).filter(
        Seed.id == purchase.seed_id
    ).first()

    if not seed:
        return None

    if seed.quantity < purchase.quantity:
        return {
            "error": "Insufficient stock"
        }

    total_price = seed.price * purchase.quantity

    new_purchase = SeedPurchase(

        buyer_id=buyer_id,

        seed_id=purchase.seed_id,

        quantity=purchase.quantity,

        total_price=total_price,

        purchase_date=purchase.purchase_date,

        status="Pending"

    )

    # Reduce Stock
    seed.quantity -= purchase.quantity

    # Increase Sold Quantity
    seed.sold_quantity += purchase.quantity

    # Update Stock Status
    if seed.quantity <= 0:
        seed.stock_status = "Out of Stock"
    else:
        seed.stock_status = "Available"

    db.add(new_purchase)

    db.commit()

    db.refresh(new_purchase)

    return new_purchase


def get_my_purchases(
    db: Session,
    buyer_id: int
):

    return db.query(SeedPurchase).filter(
        SeedPurchase.buyer_id == buyer_id
    ).all()


def get_all_purchases(
    db: Session
):

    return db.query(SeedPurchase).all()


def get_purchase_by_id(
    db: Session,
    purchase_id: int
):

    return db.query(SeedPurchase).filter(
        SeedPurchase.id == purchase_id
    ).first()


def update_purchase_status(
    db: Session,
    purchase_id: int,
    purchase: SeedPurchaseUpdate
):

    db_purchase = db.query(SeedPurchase).filter(
        SeedPurchase.id == purchase_id
    ).first()

    if not db_purchase:
        return None

    db_purchase.status = purchase.status

    db.commit()

    db.refresh(db_purchase)

    return db_purchase


def delete_purchase(
    db: Session,
    purchase_id: int
):

    db_purchase = db.query(SeedPurchase).filter(
        SeedPurchase.id == purchase_id
    ).first()

    if not db_purchase:
        return None

    db.delete(db_purchase)

    db.commit()

    return {
        "message": "Purchase deleted successfully"
    }


# Seller Sales History
def get_seller_sales(
    db: Session,
    seller_id: int
):

    return (
        db.query(SeedPurchase)
        .join(
            Seed,
            Seed.id == SeedPurchase.seed_id
        )
        .filter(
            Seed.seller_id == seller_id
        )
        .all()
    )


# Revenue Calculator
def calculate_revenue(
    db: Session,
    seller_id: int
):

    sales = (
        db.query(SeedPurchase)
        .join(
            Seed,
            Seed.id == SeedPurchase.seed_id
        )
        .filter(
            Seed.seller_id == seller_id
        )
        .all()
    )

    revenue = sum(
        sale.total_price
        for sale in sales
    )

    return {
        "total_sales": len(sales),
        "revenue": revenue
    }


# Cancel Purchase
def cancel_purchase(
    db: Session,
    purchase_id: int
):

    purchase = db.query(
        SeedPurchase
    ).filter(
        SeedPurchase.id == purchase_id
    ).first()

    if not purchase:
        return None

    seed = db.query(
        Seed
    ).filter(
        Seed.id == purchase.seed_id
    ).first()

    if seed:

        seed.quantity += purchase.quantity

        seed.sold_quantity -= purchase.quantity

        if seed.sold_quantity < 0:
            seed.sold_quantity = 0

        seed.stock_status = "Available"

    purchase.status = "Cancelled"

    db.commit()

    db.refresh(purchase)

    return purchase


# Low Stock
def low_stock(
    db: Session
):

    return (
        db.query(Seed)
        .filter(
            Seed.quantity < 20
        )
        .all()
    )