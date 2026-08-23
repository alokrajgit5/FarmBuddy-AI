from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.db.database import Base


class SeedPurchase(Base):

    __tablename__ = "seed_purchases"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    buyer_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    seed_id = Column(
        Integer,
        ForeignKey("seeds.id")
    )

    quantity = Column(Float)

    total_price = Column(Float)

    purchase_date = Column(String)

    status = Column(
        String,
        default="Pending"
    )

    buyer = relationship(
        "User"
    )

    seed = relationship(
        "Seed"
    )