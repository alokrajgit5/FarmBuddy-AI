from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.db.database import Base


class Seed(Base):

    __tablename__ = "seeds"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    seller_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    seed_name = Column(String)

    crop_name = Column(String)

    variety = Column(String)

    quantity = Column(Float)

    unit = Column(String)

    price = Column(Float)

    description = Column(String)

    image = Column(String)

    seller = relationship(
        "User"
    )
    stock_status = Column(
    String,
    default="Available"
    )

    sold_quantity = Column(
        Float,
    default=0
    )