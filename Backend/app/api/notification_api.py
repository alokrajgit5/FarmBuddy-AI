from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.dependencies.auth import get_current_user

from app.schemas.notification_schema import (
    NotificationResponse
)

from app.services.notification_service import (
    get_notifications
)

router = APIRouter(
    prefix="/api/notifications",
    tags=["Notifications"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/",
    response_model=list[NotificationResponse]
)
def notifications(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_notifications(
        db,
        current_user.id
    )