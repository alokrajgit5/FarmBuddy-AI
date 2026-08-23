from sqlalchemy.orm import Session

from app.models.labor import Labor
from app.schemas.labor_schema import (
    LaborCreate,
    LaborUpdate
)


def create_labor(
    db: Session,
    labor: LaborCreate,
    owner_id: int
):

    new_labor = Labor(

        owner_id=owner_id,

        full_name=labor.worker_name,

        phone=labor.phone,

        village=labor.village,

        district="",

        state="",

        skill=labor.work_type,

        experience=labor.experience,

        daily_wage=labor.daily_wage,

        available=labor.available

    )

    db.add(new_labor)

    db.commit()

    db.refresh(new_labor)

    return new_labor


def get_all_labors(db: Session):

    return db.query(Labor).all()


def get_labor_by_id(
    db: Session,
    labor_id: int
):

    return db.query(Labor).filter(

        Labor.id == labor_id

    ).first()


def update_labor(
    db: Session,
    labor_id: int,
    labor: LaborUpdate
):

    db_labor = db.query(Labor).filter(

        Labor.id == labor_id

    ).first()

    if not db_labor:

        return None

    update_data = labor.model_dump(exclude_unset=True)

    if "worker_name" in update_data:
        db_labor.full_name = update_data["worker_name"]

    if "phone" in update_data:
        db_labor.phone = update_data["phone"]

    if "village" in update_data:
        db_labor.village = update_data["village"]

    if "work_type" in update_data:
        db_labor.skill = update_data["work_type"]

    if "experience" in update_data:
        db_labor.experience = update_data["experience"]

    if "daily_wage" in update_data:
        db_labor.daily_wage = update_data["daily_wage"]

    if "available" in update_data:
        db_labor.available = update_data["available"]

    db.commit()

    db.refresh(db_labor)

    return db_labor


def delete_labor(
    db: Session,
    labor_id: int
):

    db_labor = db.query(Labor).filter(

        Labor.id == labor_id

    ).first()

    if not db_labor:

        return None

    db.delete(db_labor)

    db.commit()

    return {
        "message": "Labor deleted successfully"
    }