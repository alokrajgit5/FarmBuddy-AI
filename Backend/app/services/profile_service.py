from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.schemas.profile_schema import ProfileCreate


def create_profile(
    db: Session,
    profile: ProfileCreate,
    user_id: int
):

    new_profile = Profile(

        user_id=user_id,

        phone=profile.phone,

        state=profile.state,

        district=profile.district,

        village=profile.village,

        land_area=profile.land_area,

        soil_type=profile.soil_type,

        main_crop=profile.main_crop,

        irrigation=profile.irrigation,

        experience=profile.experience,

        bio=profile.bio,

        profile_image=profile.profile_image

    )

    db.add(new_profile)

    db.commit()

    db.refresh(new_profile)

    return new_profile
def get_profile(
    db: Session,
    user_id: int
):

    return db.query(Profile).filter(

        Profile.user_id == user_id

    ).first()
def update_profile(
    db: Session,
    user_id: int,
    profile: ProfileCreate
):

    db_profile = db.query(Profile).filter(

        Profile.user_id == user_id

    ).first()

    if not db_profile:

        return None

    db_profile.phone = profile.phone

    db_profile.state = profile.state

    db_profile.district = profile.district

    db_profile.village = profile.village

    db_profile.land_area = profile.land_area

    db_profile.soil_type = profile.soil_type

    db_profile.main_crop = profile.main_crop

    db_profile.irrigation = profile.irrigation

    db_profile.experience = profile.experience

    db_profile.bio = profile.bio

    db_profile.profile_image = profile.profile_image

    db.commit()

    db.refresh(db_profile)

    return db_profile