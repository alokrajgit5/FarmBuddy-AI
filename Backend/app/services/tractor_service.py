from sqlalchemy.orm import Session

from app.models.tractor import Tractor
from app.schemas.tractor_schema import TractorCreate


def create_tractor(
    db: Session,
    tractor: TractorCreate
):

    new_tractor = Tractor(

        tractor_name=tractor.tractor_name,

        brand=tractor.brand,

        model=tractor.model,

        rent_per_day=tractor.rent_per_day,

        location=tractor.location,

        owner_name=tractor.owner_name,

        owner_phone=tractor.owner_phone,

        description=tractor.description

    )

    db.add(new_tractor)

    db.commit()

    db.refresh(new_tractor)

    return new_tractor


def get_all_tractors(db: Session):

    return db.query(Tractor).all()


def get_tractor(
    db: Session,
    tractor_id: int
):

    return db.query(Tractor).filter(

        Tractor.id == tractor_id

    ).first()


def update_tractor(
    db: Session,
    tractor_id: int,
    tractor: TractorCreate
):

    db_tractor = db.query(Tractor).filter(

        Tractor.id == tractor_id

    ).first()

    if not db_tractor:

        return None

    db_tractor.tractor_name = tractor.tractor_name
    db_tractor.brand = tractor.brand
    db_tractor.model = tractor.model
    db_tractor.rent_per_day = tractor.rent_per_day
    db_tractor.location = tractor.location
    db_tractor.owner_name = tractor.owner_name
    db_tractor.owner_phone = tractor.owner_phone
    db_tractor.description = tractor.description

    db.commit()

    db.refresh(db_tractor)

    return db_tractor


def delete_tractor(
    db: Session,
    tractor_id: int
):

    db_tractor = db.query(Tractor).filter(

        Tractor.id == tractor_id

    ).first()

    if not db_tractor:

        return False

    db.delete(db_tractor)

    db.commit()

    return True