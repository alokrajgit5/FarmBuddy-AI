from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class LaborBooking(Base):
    __tablename__ = "labor_bookings"

    id = Column(Integer, primary_key=True, index=True)

    farmer_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    labor_id = Column(
        Integer,
        ForeignKey("labors.id")
    )

    booking_date = Column(String)

    working_days = Column(Integer)

    total_amount = Column(Float)

    status = Column(
        String,
        default="Pending"
    )

    farmer = relationship(
        "User"
    )

    labor = relationship(
        "Labor"
    )