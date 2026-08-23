from fastapi import APIRouter

from app.services.email_service import send_email

router = APIRouter(
    prefix="/api/email",
    tags=["Email"]
)


@router.get("/test")
async def test_email():

    await send_email(
        recipient="YOUR_EMAIL@gmail.com",
        subject="FarmBuddy AI Test",
        body="""
        <h2>Email Working Successfully ✅</h2>
        <p>This email was sent from FarmBuddy AI.</p>
        """
    )

    return {
        "message": "Email sent successfully."
    }
