import os
import uuid
from io import BytesIO

from PIL import Image

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from app.schemas.disease_schema import DiseaseResponse
from app.services.disease_service import detect_disease

router = APIRouter(
    prefix="/api/disease",
    tags=["Disease Detection"]
)

UPLOAD_FOLDER = "uploads/disease_images"

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


@router.post(
    "/predict",
    response_model=DiseaseResponse
)
async def predict_disease(
    image: UploadFile = File(...)
):

    allowed_extensions = [
        ".jpg",
        ".jpeg",
        ".png"
    ]

    extension = os.path.splitext(
        image.filename
    )[1].lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, JPEG and PNG images are allowed."
        )

    image_bytes = await image.read()

    if len(image_bytes) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="Image size must be less than 5 MB."
        )

    try:

        img = Image.open(
            BytesIO(image_bytes)
        )

        img.verify()

    except Exception:

        raise HTTPException(
            status_code=400,
            detail="Invalid or corrupted image."
        )

    img = Image.open(
        BytesIO(image_bytes)
    )

    width, height = img.size

    if width < 100 or height < 100:

        raise HTTPException(
            status_code=400,
            detail="Image resolution is too small."
        )

    os.makedirs(
        UPLOAD_FOLDER,
        exist_ok=True
    )

    filename = (
        f"{uuid.uuid4()}{extension}"
    )

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    with open(
        filepath,
        "wb"
    ) as buffer:

        buffer.write(image_bytes)

    result = detect_disease()

    return result