from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base


class DiseaseDetection(Base):
    __tablename__ = "disease_detections"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    image_path = Column(String, nullable=False)

    disease_name = Column(String, nullable=False)

    confidence = Column(String, nullable=False)

    treatment = Column(String, nullable=False)