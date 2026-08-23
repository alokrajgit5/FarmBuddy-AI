from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.database import Base


class Soil(Base):
    __tablename__ = "soil"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    nitrogen = Column(Float)

    phosphorus = Column(Float)

    potassium = Column(Float)

    ph = Column(Float)

    moisture = Column(Float)

    recommendation = Column(String)