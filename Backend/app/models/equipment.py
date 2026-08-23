from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.db.database import Base


class Equipment(Base):

    __tablename__ = "equipments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    equipment_name = Column(
        String,
        nullable=False
    )

    category = Column(
        String,
        nullable=False
    )

    brand = Column(
        String,
        nullable=True
    )

    model = Column(
        String,
        nullable=True
    )

    price_per_day = Column(
        Float,
        nullable=False
    )

    location = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    image = Column(
        String,
        nullable=True
    )

    availability = Column(
        String,
        default="Available"
    )

    owner = relationship(
        "User"
    )