from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.db.database import Base, engine

# Models
from app.models.user import User
from app.models.profile import Profile
from app.models.crop import Crop
from app.api.tractor_api import router as tractor_router
from app.api.tractor_booking_api import router as tractor_booking_router
from app.models.soil import Soil

# Routers
from app.api.user_api import router as user_router
from app.models.seed import Seed
from app.api.profile_api import router as profile_router
from app.api.crop_api import router as crop_router
from app.api.seed_api import router as seed_router
from app.models.labor import Labor
from app.api.weather_api import router as weather_router
from app.api.soil_api import router as soil_router
from app.api.recommendation_api import router as recommendation_router
from app.api.disease_api import router as disease_router
from app.api.fertilizer_api import router as fertilizer_router
from app.api.labor_api import router as labor_router
from app.api.crop_recommendation_api import router as crop_recommendation_router
from app.api.scheme_api import router as scheme_router
from app.api.chat_api import router as chat_router
from app.models.equipment import Equipment
from app.api.dashboard_api import router as dashboard_router
from app.api.notification_api import router as notification_router
from app.models.seed_purchase import SeedPurchase
from app.api.equipment_api import router as equipment_router
from app.api.seed_purchase_api import router as seed_purchase_router
from app.models.labor_booking import LaborBooking
from app.models.equipment_review import EquipmentReview
from app.api.upload_api import router as upload_router
from app.api.email_api import router as email_router
from app.api.password_api import router as password_router
from app.api.verification_api import router as verification_router
from app.models.payment import Payment
from app.api.equipment_booking_api import router as equipment_booking_router
from app.models.equipment_booking import EquipmentBooking
from app.api.labor_booking_api import router as labor_booking_router
from app.api.voice_api import router as voice_router
from app.api.payment_api import router as payment_router
from app.api.equipment_review_api import router as equipment_review_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FarmBuddy AI",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static Folder
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

# Home
@app.get("/")
def home():
    return {
        "message": "FarmBuddy AI Backend Connected Successfully"
    }

# Routers
app.include_router(
    user_router,
    prefix="/api/users",
    tags=["Users"]
)

app.include_router(profile_router)
app.include_router(equipment_review_router)
app.include_router(crop_router)
app.include_router(weather_router)
app.include_router(soil_router)
app.include_router(recommendation_router)
app.include_router(disease_router)
app.include_router(fertilizer_router)
app.include_router(equipment_booking_router)
app.include_router(equipment_router)
app.include_router(crop_recommendation_router)
app.include_router(scheme_router)
app.include_router(chat_router)
app.include_router(dashboard_router)
app.include_router(seed_purchase_router)
app.include_router(notification_router)
app.include_router(upload_router)
app.include_router(labor_router)
app.include_router(email_router)
app.include_router(labor_booking_router)
app.include_router(password_router)
app.include_router(verification_router)
app.include_router(seed_router)
app.include_router(voice_router)
app.include_router(tractor_router)
app.include_router(tractor_booking_router)
app.include_router(payment_router)