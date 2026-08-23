from sqlalchemy.orm import Session

from app.models.equipment import Equipment

from app.schemas.equipment_schema import (
    EquipmentCreate,
    EquipmentUpdate
)


def create_equipment(
    db: Session,
    equipment: EquipmentCreate,
    owner_id: int
):

    new_equipment = Equipment(

        owner_id=owner_id,

        equipment_name=equipment.equipment_name,

        category=equipment.category,

        brand=equipment.brand,

        model=equipment.model,

        price_per_day=equipment.price_per_day,

        location=equipment.location,

        description=equipment.description,

        image=equipment.image,

        availability="Available"

    )

    db.add(new_equipment)

    db.commit()

    db.refresh(new_equipment)

    return new_equipment


def get_all_equipment(
    db: Session
):

    return db.query(Equipment).all()


def get_equipment_by_id(
    db: Session,
    equipment_id: int
):

    return db.query(Equipment).filter(

        Equipment.id == equipment_id

    ).first()


def update_equipment(
    db: Session,
    equipment_id: int,
    equipment: EquipmentUpdate
):

    db_equipment = db.query(Equipment).filter(

        Equipment.id == equipment_id

    ).first()

    if not db_equipment:

        return None

    db_equipment.equipment_name = equipment.equipment_name
    db_equipment.category = equipment.category
    db_equipment.brand = equipment.brand
    db_equipment.model = equipment.model
    db_equipment.price_per_day = equipment.price_per_day
    db_equipment.location = equipment.location
    db_equipment.description = equipment.description
    db_equipment.image = equipment.image
    db_equipment.availability = equipment.availability

    db.commit()

    db.refresh(db_equipment)

    return db_equipment


def delete_equipment(
    db: Session,
    equipment_id: int
):

    db_equipment = db.query(Equipment).filter(

        Equipment.id == equipment_id

    ).first()

    if not db_equipment:

        return None

    db.delete(db_equipment)

    db.commit()

    return {
        "message": "Equipment deleted successfully"
    }


def get_equipment_by_category(
    db: Session,
    category: str
):

    return db.query(Equipment).filter(

        Equipment.category == category

    ).all()


def get_equipment_by_location(
    db: Session,
    location: str
):

    return db.query(Equipment).filter(

        Equipment.location == location

    ).all()


def get_available_equipment(
    db: Session
):

    return db.query(Equipment).filter(

        Equipment.availability == "Available"

    ).all()


def get_my_equipment(
    db: Session,
    owner_id: int
):

    return db.query(Equipment).filter(

        Equipment.owner_id == owner_id

    ).all()