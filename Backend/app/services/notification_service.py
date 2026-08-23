from datetime import datetime

from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.models.crop import Crop


def get_notifications(
    db: Session,
    user_id: int
):

    notifications = []

    profile = db.query(Profile).filter(
        Profile.user_id == user_id
    ).first()

    crops = db.query(Crop).filter(
        Crop.owner_id == user_id
    ).all()

    now = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Profile
    if not profile:
        notifications.append({
            "title": "Complete Profile",
            "message": "Please complete your farmer profile.",
            "notification_type": "profile",
            "priority": "high",
            "created_at": now
        })

    # Crop
    if not crops:
        notifications.append({
            "title": "Register Crop",
            "message": "Add your first crop.",
            "notification_type": "crop",
            "priority": "high",
            "created_at": now
        })
    else:
        notifications.append({
            "title": "Crop Summary",
            "message": f"You have {len(crops)} crop(s).",
            "notification_type": "crop",
            "priority": "medium",
            "created_at": now
        })

    # Irrigation
    if profile and profile.irrigation:
        notifications.append({
            "title": "Irrigation Reminder",
            "message": (
                f"Current irrigation: "
                f"{profile.irrigation}"
            ),
            "notification_type": "irrigation",
            "priority": "medium",
            "created_at": now
        })

    # Weather
    notifications.append({
        "title": "Weather Alert",
        "message": (
            "Check today's weather "
            "before field work."
        ),
        "notification_type": "weather",
        "priority": "low",
        "created_at": now
    })

    # Fertilizer
    notifications.append({
        "title": "Fertilizer Reminder",
        "message": (
            "Review fertilizer "
            "requirements this week."
        ),
        "notification_type": "fertilizer",
        "priority": "medium",
        "created_at": now
    })

    return notifications