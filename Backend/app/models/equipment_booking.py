from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    ForeignKey,
    Date
)

from sqlalchemy.orm import relationship

from app.db.database import Base


class EquipmentBooking(Base):

    __tablename__ = "equipment_bookings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    equipment_id = Column(
        Integer,
        ForeignKey("equipments.id")
    )

    renter_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    start_date = Column(
        Date,
        nullable=False
    )

    end_date = Column(
        Date,
        nullable=False
    )

    total_days = Column(
        Integer,
        nullable=False
    )

    total_amount = Column(
        Float,
        nullable=False
    )

    status = Column(
        String,
        default="Pending"
    )

    equipment = relationship(
        "Equipment"
    )

    renter = relationship(
        "User"
    )