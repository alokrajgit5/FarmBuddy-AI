from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Tractor(Base):
    __tablename__ = "tractors"

    id = Column(Integer, primary_key=True, index=True)

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    tractor_name = Column(String)

    company = Column(String)

    horsepower = Column(Integer)

    rent_per_day = Column(Float)

    location = Column(String)

    status = Column(
        String,
        default="Available"
    )

    owner = relationship(
    "User",
    back_populates="tractors"
    )

    bookings = relationship(
        "TractorBooking",
        back_populates="tractor",
        cascade="all, delete"
    )