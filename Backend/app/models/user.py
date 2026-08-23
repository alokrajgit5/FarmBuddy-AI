from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password = Column(String, nullable=False)

    is_verified = Column(
        Boolean,
        default=False
    )

    crops = relationship(
        "Crop",
        back_populates="owner",
        cascade="all, delete"
    )

    profile = relationship(
        "Profile",
        back_populates="user",
        uselist=False,
        cascade="all, delete"
    )
    tractors = relationship(
    "Tractor",
    back_populates="owner"
    )

    tractor_bookings = relationship(
        "TractorBooking"
    )