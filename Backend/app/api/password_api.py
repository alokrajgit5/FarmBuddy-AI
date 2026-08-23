from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.user import User

from app.schemas.password_schema import (
    ForgotPasswordRequest,
    ResetPasswordRequest
)

from app.services.email_service import send_email

from app.utils.jwt import (
    create_access_token,
    verify_token
)

from app.utils.security import hash_password


router = APIRouter(
    prefix="/api/password",
    tags=["Password"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/forgot")
async def forgot_password(
    request: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.email == request.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    token = create_access_token(
        {"sub": user.email}
    )

    body = f"""
    <h2>FarmBuddy AI Password Reset</h2>

    <p>Your password reset token is:</p>

    <h3>{token}</h3>

    <p>Use this token to reset your password.</p>
    """

    await send_email(
        recipient=user.email,
        subject="Password Reset",
        body=body
    )

    return {
        "message": "Password reset email sent."
    }


@router.post("/reset")
def reset_password(
    request: ResetPasswordRequest,
    db: Session = Depends(get_db)
):
    payload = verify_token(
        request.token
    )

    email = payload.get("sub")

    if not email:
        raise HTTPException(
            status_code=400,
            detail="Invalid token."
        )

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    user.password = hash_password(
        request.new_password
    )

    db.commit()

    return {
        "message": "Password reset successfully."
    }