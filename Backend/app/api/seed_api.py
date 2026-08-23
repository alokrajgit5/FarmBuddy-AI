from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.seed_schema import (
    SeedCreate,
    SeedUpdate,
    SeedResponse
)

from app.services.seed_service import (
    create_seed,
    get_all_seeds,
    get_seed_by_id,
    update_seed,
    delete_seed
)

router = APIRouter(
    prefix="/api/seeds",
    tags=["Seed Marketplace"]
)


@router.post(
    "/",
    response_model=SeedResponse
)
def add_seed(
    seed: SeedCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_seed(
        db,
        seed,
        current_user.id
    )


@router.get(
    "/",
    response_model=list[SeedResponse]
)
def all_seeds(
    db: Session = Depends(get_db)
):

    return get_all_seeds(db)


@router.get(
    "/{seed_id}",
    response_model=SeedResponse
)
def single_seed(
    seed_id: int,
    db: Session = Depends(get_db)
):

    seed = get_seed_by_id(
        db,
        seed_id
    )

    if not seed:
        raise HTTPException(
            status_code=404,
            detail="Seed not found"
        )

    return seed


@router.put(
    "/{seed_id}",
    response_model=SeedResponse
)
def edit_seed(
    seed_id: int,
    seed: SeedUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    updated = update_seed(
        db,
        seed_id,
        seed
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Seed not found"
        )

    return updated


@router.delete(
    "/{seed_id}"
)
def remove_seed(
    seed_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    deleted = delete_seed(
        db,
        seed_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Seed not found"
        )

    return deleted