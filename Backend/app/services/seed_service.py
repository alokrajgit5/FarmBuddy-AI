from sqlalchemy.orm import Session

from app.models.seed import Seed

from app.schemas.seed_schema import (
    SeedCreate,
    SeedUpdate
)


def create_seed(
    db: Session,
    seed: SeedCreate,
    seller_id: int
):

    new_seed = Seed(

        seller_id=seller_id,

        seed_name=seed.seed_name,

        crop_name=seed.crop_name,

        variety=seed.variety,

        quantity=seed.quantity,

        unit=seed.unit,

        price=seed.price,

        description=seed.description,

        image=seed.image

    )

    db.add(new_seed)

    db.commit()

    db.refresh(new_seed)

    return new_seed


def get_all_seeds(
    db: Session
):

    return db.query(Seed).all()


def get_seed_by_id(
    db: Session,
    seed_id: int
):

    return db.query(Seed).filter(

        Seed.id == seed_id

    ).first()


def update_seed(
    db: Session,
    seed_id: int,
    seed: SeedUpdate
):

    db_seed = db.query(Seed).filter(

        Seed.id == seed_id

    ).first()

    if not db_seed:

        return None

    db_seed.seed_name = seed.seed_name

    db_seed.crop_name = seed.crop_name

    db_seed.variety = seed.variety

    db_seed.quantity = seed.quantity

    db_seed.unit = seed.unit

    db_seed.price = seed.price

    db_seed.description = seed.description

    db_seed.image = seed.image

    db.commit()

    db.refresh(db_seed)

    return db_seed


def delete_seed(
    db: Session,
    seed_id: int
):

    db_seed = db.query(Seed).filter(

        Seed.id == seed_id

    ).first()

    if not db_seed:

        return None

    db.delete(db_seed)

    db.commit()

    return {

        "message": "Seed deleted successfully"

    }