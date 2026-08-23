from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Date
)

from sqlalchemy.orm import relationship

from app.db.database import Base


class TractorBooking(Base):
    __tablename__ = "tractor_bookings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    tractor_id = Column(
        Integer,
        ForeignKey("tractors.id")
    )

    farmer_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    booking_date = Column(
        Date
    )

    total_days = Column(
        Integer
    )

    message = Column(
        String,
        nullable=True
    )

    status = Column(
        String,
        default="Pending"
    )

    tractor = relationship(
        "Tractor",
        back_populates="bookings"
    )

    farmer = relationship(
        "User"
    )