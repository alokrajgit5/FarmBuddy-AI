from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.dependencies.auth import get_current_user

from app.models.profile import Profile

from app.services.upload_service import (
    save_profile_image
)

router = APIRouter(
    prefix="/api/upload",
    tags=["Upload"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/profile")
def upload_profile_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    profile = db.query(Profile).filter(
        Profile.user_id == current_user.id
    ).first()

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found."
        )

    filename = save_profile_image(file)

    profile.profile_image = filename

    db.commit()
    db.refresh(profile)

    return {
        "message": "Profile image uploaded successfully.",
        "filename": filename,
        "image_url": f"/uploads/profiles/{filename}"
    }