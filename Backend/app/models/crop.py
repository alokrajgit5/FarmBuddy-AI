from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Crop(Base):
    __tablename__ = "crops"

    id = Column(Integer, primary_key=True, index=True)

    crop_name = Column(String, nullable=False)

    season = Column(String, nullable=False)

    area = Column(Float, nullable=False)

    irrigation = Column(String, nullable=False)

    fertilizer = Column(String, nullable=False)

    expected_yield = Column(Float, nullable=False)

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    owner = relationship(
        "User",
        back_populates="crops"
    )