from pydantic import BaseModel


class NotificationResponse(BaseModel):
    title: str
    message: str
    notification_type: str
    priority: str
    created_at: str