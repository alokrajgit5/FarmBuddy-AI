from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.user import User

from app.utils.jwt import (
    create_access_token,
    verify_token
)

from app.services.email_service import (
    send_email
)

router = APIRouter(
    prefix="/api/verification",
    tags=["Verification"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/send/{email}")
async def send_verification(
    email: str,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    token = create_access_token(
        {"sub": user.email}
    )

    verify_url = (
        f"http://127.0.0.1:8000/api/verification/verify/{token}"
    )

    body = f"""
    <h2>Verify Your Email</h2>

    <p>Click below:</p>

    <a href="{verify_url}">
        Verify Email
    </a>
    """

    await send_email(
        recipient=user.email,
        subject="Verify Your Email",
        body=body
    )

    return {
        "message": "Verification email sent."
    }


@router.get("/verify/{token}")
def verify_email(
    token: str,
    db: Session = Depends(get_db)
):

    payload = verify_token(token)

    email = payload.get("sub")

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    user.is_verified = True

    db.commit()

    return {
        "message": "Email verified successfully."
    }