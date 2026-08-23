from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal

from app.schemas.tractor_schema import (
    TractorCreate,
    TractorResponse
)

from app.services.tractor_service import (
    create_tractor,
    get_all_tractors,
    get_tractor,
    update_tractor,
    delete_tractor
)

router = APIRouter(

    prefix="/api/tractors",

    tags=["Tractor Rental"]

)


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@router.post(

    "/",

    response_model=TractorResponse

)
def add_tractor(

    tractor: TractorCreate,

    db: Session = Depends(get_db)

):

    return create_tractor(

        db,

        tractor

    )


@router.get(

    "/",

    response_model=list[TractorResponse]

)
def tractors(

    db: Session = Depends(get_db)

):

    return get_all_tractors(db)


@router.get(

    "/{tractor_id}",

    response_model=TractorResponse

)
def tractor(

    tractor_id: int,

    db: Session = Depends(get_db)

):

    tractor = get_tractor(

        db,

        tractor_id

    )

    if not tractor:

        raise HTTPException(

            status_code=404,

            detail="Tractor not found"

        )

    return tractor


@router.put(

    "/{tractor_id}",

    response_model=TractorResponse

)
def edit_tractor(

    tractor_id: int,

    tractor: TractorCreate,

    db: Session = Depends(get_db)

):

    updated = update_tractor(

        db,

        tractor_id,

        tractor

    )

    if not updated:

        raise HTTPException(

            status_code=404,

            detail="Tractor not found"

        )

    return updated


@router.delete(

    "/{tractor_id}"

)
def remove_tractor(

    tractor_id: int,

    db: Session = Depends(get_db)

):

    deleted = delete_tractor(

        db,

        tractor_id

    )

    if not deleted:

        raise HTTPException(

            status_code=404,

            detail="Tractor not found"

        )

    return {

        "message": "Tractor deleted successfully"

    }