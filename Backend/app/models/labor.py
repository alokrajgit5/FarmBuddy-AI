from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.db.database import Base


class Labor(Base):
    __tablename__ = "labors"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    full_name = Column(
        String,
        nullable=False
    )

    phone = Column(
        String,
        nullable=False
    )

    village = Column(
        String,
        nullable=False
    )

    district = Column(
        String,
        nullable=False
    )

    state = Column(
        String,
        nullable=False
    )

    skill = Column(
        String,
        nullable=False
    )

    experience = Column(
        Integer,
        default=0
    )

    daily_wage = Column(
        Float,
        nullable=False
    )

    available = Column(
        Boolean,
        default=True
    )

    owner = relationship(
        "User",
        backref="labors"
    )