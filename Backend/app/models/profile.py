from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True
    )

    phone = Column(String)

    state = Column(String)

    district = Column(String)

    village = Column(String)

    land_area = Column(Float)

    soil_type = Column(String)

    main_crop = Column(String)

    irrigation = Column(String)

    experience = Column(String)

    bio = Column(String)

    profile_image = Column(String)

    user = relationship(
        "User",
        back_populates="profile"
    )