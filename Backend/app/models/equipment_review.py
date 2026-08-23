from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.database import Base


class EquipmentReview(Base):

    __tablename__ = "equipment_reviews"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    equipment_id = Column(
        Integer,
        ForeignKey("equipments.id"),
        nullable=False
    )

    reviewer_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    rating = Column(
        Integer,
        nullable=False
    )

    review = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    equipment = relationship(
        "Equipment"
    )

    reviewer = relationship(
        "User"
    )