from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.db.database import get_db
from app.schemas.user_schema import UserCreate, UserLogin
from app.services.user_service import (
    create_user,
    login_user,
)

router = APIRouter()


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return create_user(db, user)


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    return login_user(db, user)
@router.get("/me")
def current_user(

    user: User = Depends(get_current_user)

):

    return {

        "id": user.id,

        "full_name": user.full_name,

        "email": user.email

    }