from datetime import datetime
from calendar import month_abbr
from collections import defaultdict
from random import choice

from sqlalchemy import desc, func
from sqlalchemy.orm import Session

# ============================================================
# MODELS
# ============================================================

from app.models.user import User
from app.models.profile import Profile
from app.models.crop import Crop

from app.models.tractor import Tractor
from app.models.tractor_booking import TractorBooking

from app.models.labor import Labor
from app.models.labor_booking import LaborBooking

from app.models.seed import Seed
from app.models.seed_purchase import SeedPurchase

from app.models.payment import Payment

# ============================================================
# SERVICES
# ============================================================

from app.services.weather_service import get_weather
from app.services.crop_health_service import calculate_crop_health


# ============================================================
# CONSTANTS
# ============================================================

DEFAULT_CITY = "Delhi"

AI_TIPS = [
    "Monitor soil moisture regularly.",
    "Use organic fertilizer.",
    "Avoid over irrigation.",
    "Inspect crops every week.",
    "Apply disease prevention spray.",
]

FARMER_NEWS = [
    {
        "title": "Government announces new subsidy for farmers.",
        "category": "Government",
        "time": "2 hours ago",
    },
    {
        "title": "Rain expected this week.",
        "category": "Weather",
        "time": "Today",
    },
    {
        "title": "AI technology improves crop disease detection.",
        "category": "Technology",
        "time": "Yesterday",
    },
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def _safe_float(value, default=0.0) -> float:
    """
    Safely convert a value to float.
    """
    try:
        if value is None:
            return default

        return float(value)

    except (TypeError, ValueError):
        return default


def _safe_int(value, default=0) -> int:
    """
    Safely convert a value to int.
    """
    try:
        if value is None:
            return default

        return int(value)

    except (TypeError, ValueError):
        return default


def _safe_date_string(value) -> str:
    """
    Convert datetime/date/string safely to string.
    """
    if value is None:
        return ""

    try:
        if hasattr(value, "strftime"):
            return value.strftime("%Y-%m-%d")

    except Exception:
        pass

    return str(value)


def _get_month_from_date(value):
    """
    Return month abbreviation such as Jan, Feb, Mar.
    """
    if value is None:
        return None

    try:
        if hasattr(value, "month"):
            month_number = int(value.month)

            if 1 <= month_number <= 12:
                return month_abbr[month_number]

    except Exception:
        pass

    # Try common string date formats.
    if isinstance(value, str):

        formats = [
            "%Y-%m-%d",
            "%Y/%m/%d",
            "%d-%m-%Y",
            "%d/%m/%Y",
            "%Y-%m-%d %H:%M:%S",
            "%Y/%m/%d %H:%M:%S",
        ]

        for date_format in formats:

            try:
                parsed = datetime.strptime(
                    value,
                    date_format,
                )

                return parsed.strftime("%b")

            except ValueError:
                continue

    return None


def _empty_monthly_booking_graph():
    """
    Return a complete Jan-Dec booking graph.
    """
    return [
        {
            "month": month_abbr[index],
            "count": 0,
        }
        for index in range(1, 13)
    ]


def _empty_income_expense_chart():
    """
    Return a complete Jan-Dec finance chart.
    """
    return [
        {
            "month": month_abbr[index],
            "income": 0.0,
            "expense": 0.0,
        }
        for index in range(1, 13)
    ]


def _get_ai_health_status(score: int) -> str:
    """
    Convert AI score into a readable status.
    """
    if score >= 90:
        return "Excellent"

    if score >= 75:
        return "Good"

    return "Average"


def _get_weather_animation(temperature: float):
    """
    Build dashboard weather animation information.
    """
    if temperature >= 35:
        icon = "☀️"
        gradient = "sunny"

    elif temperature >= 30:
        icon = "🌤️"
        gradient = "sunny"

    elif temperature >= 20:
        icon = "⛅"
        gradient = "cloudy"

    else:
        icon = "🌥️"
        gradient = "cool"

    return {
        "icon": icon,
        "gradient": gradient,
        "feels_like": round(temperature + 2, 1),
        "visibility": 10,
        "uv_index": 6,
        "sunrise": "05:32 AM",
        "sunset": "06:48 PM",
    }


# ============================================================
# MAIN DASHBOARD SERVICE
# ============================================================

def get_dashboard(
    db: Session,
    user_id: int,
):
    """
    Build the complete FarmBuddy AI farmer dashboard.

    Important:
    This function returns the fields required by
    app.schemas.dashboard_schema.DashboardResponse.
    """

    # ========================================================
    # 1. CURRENT USER
    # ========================================================

    user = (
        db.query(User)
        .filter(
            User.id == user_id
        )
        .first()
    )

    if not user:
        return {
            "status": "error",
            "message": "User not found",
        }

    farmer_name = (
        getattr(user, "full_name", None)
        or "Farmer"
    )

    # ========================================================
    # 2. FARMER PROFILE
    # ========================================================

    profile = (
        db.query(Profile)
        .filter(
            Profile.user_id == user_id
        )
        .first()
    )

    profile_completion = 0

    if profile:

        profile_fields = [
            getattr(profile, "phone", None),
            getattr(profile, "state", None),
            getattr(profile, "district", None),
            getattr(profile, "village", None),
            getattr(profile, "land_area", None),
            getattr(profile, "soil_type", None),
            getattr(profile, "main_crop", None),
            getattr(profile, "irrigation", None),
            getattr(profile, "experience", None),
            getattr(profile, "bio", None),
        ]

        filled_fields = sum(
            1
            for value in profile_fields
            if value not in (None, "")
        )

        profile_completion = int(
            (
                filled_fields
                / len(profile_fields)
            )
            * 100
        )

    # ========================================================
    # 3. CROPS
    # ========================================================

    crops = (
        db.query(Crop)
        .filter(
            Crop.owner_id == user_id
        )
        .all()
    )

    total_crops = len(crops)

    total_land = sum(
        _safe_float(
            getattr(crop, "area", 0)
        )
        for crop in crops
    )

    active_crops = total_crops

    # ========================================================
    # 4. CROP HEALTH
    # ========================================================

    try:

        crop_health = calculate_crop_health(
            total_crops
        )

    except Exception:

        crop_health = {
            "health_score": 0,
            "health_status": "Unknown",
            "disease_risk": "Unknown",
            "recommendation": (
                "Unable to calculate crop health."
            ),
        }

    crop_health_score = _safe_int(
        crop_health.get(
            "health_score",
            0,
        )
    )

    crop_health_status = str(
        crop_health.get(
            "health_status",
            "Unknown",
        )
    )

    disease_risk = str(
        crop_health.get(
            "disease_risk",
            "Unknown",
        )
    )

    crop_recommendation = str(
        crop_health.get(
            "recommendation",
            "Monitor your crops regularly.",
        )
    )

    # ========================================================
    # 5. WEATHER
    # ========================================================

    city = DEFAULT_CITY

    if profile:

        profile_city = (
            getattr(profile, "district", None)
            or getattr(profile, "city", None)
        )

        if profile_city:
            city = str(profile_city)

    try:

        weather = get_weather(city)

    except Exception:

        weather = None

    if weather:

        temperature = _safe_float(
            weather.get(
                "temperature",
                0,
            )
        )

        humidity = _safe_int(
            weather.get(
                "humidity",
                0,
            )
        )

        wind_speed = _safe_float(
            weather.get(
                "wind_speed",
                0,
            )
        )

        weather_status = str(
            weather.get(
                "weather",
                "Clear",
            )
        )

        weather_city = str(
            weather.get(
                "city",
                city,
            )
        )

    else:

        temperature = 0.0
        humidity = 0
        wind_speed = 0.0
        weather_status = "Unavailable"
        weather_city = city

    city = weather_city

    updated_at = datetime.now().strftime(
        "%I:%M %p"
    )

    current_date = datetime.now().strftime(
        "%d %B %Y"
    )

    weather_card = {
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "city": city,
        "status": weather_status,
        "updated_at": updated_at,
    }

    # ========================================================
    # 6. TRACTOR BOOKINGS COUNT
    # ========================================================

    tractor_bookings = (
        db.query(TractorBooking)
        .filter(
            TractorBooking.farmer_id == user_id
        )
        .count()
    )

    # ========================================================
    # 7. LABOR BOOKINGS COUNT
    # ========================================================

    labor_bookings = (
        db.query(LaborBooking)
        .filter(
            LaborBooking.farmer_id == user_id
        )
        .count()
    )

    # ========================================================
    # 8. SEED PURCHASE COUNT
    # ========================================================

    seed_purchases = (
        db.query(SeedPurchase)
        .filter(
            SeedPurchase.buyer_id == user_id
        )
        .count()
    )

    # ========================================================
    # 9. TOTAL BOOKINGS
    # ========================================================

    total_bookings = (
        tractor_bookings
        + labor_bookings
        + seed_purchases
    )

    # ========================================================
    # 10. INCOME
    # ========================================================

    income_result = (
        db.query(
            func.coalesce(
                func.sum(
                    Payment.amount
                ),
                0,
            )
        )
        .filter(
            Payment.user_id == user_id,
            Payment.payment_status == "Completed",
        )
        .scalar()
    )

    income = _safe_float(
        income_result
    )

    # ========================================================
    # 11. SEED EXPENSES
    # ========================================================

    seed_expense_result = (
        db.query(
            func.coalesce(
                func.sum(
                    SeedPurchase.total_price
                ),
                0,
            )
        )
        .filter(
            SeedPurchase.buyer_id == user_id
        )
        .scalar()
    )

    seed_expenses = _safe_float(
        seed_expense_result
    )

    # ========================================================
    # 12. TOTAL EXPENSES
    # ========================================================
    #
    # Currently SeedPurchase is the confirmed expense source
    # from the provided models/code.
    #
    # Tractor/labor prices are not assumed here because their
    # exact price fields were not provided.
    # ========================================================

    expenses = seed_expenses

    # ========================================================
    # 13. TOTAL SPENDING / PROFIT
    # ========================================================

    total_spending = expenses

    profit = income - expenses

    # ========================================================
    # 14. AI SCORE
    # ========================================================

    ai_score = min(
        100,
        70
        + (
            total_crops * 3
        )
        + (
            profile_completion // 10
        ),
    )

    ai_score = _safe_int(
        ai_score
    )

    # ========================================================
    # 15. AI TIP
    # ========================================================

    ai_tip = choice(
        AI_TIPS
    )

    # ========================================================
    # 16. NOTIFICATIONS
    # ========================================================

    notification_count = (
        tractor_bookings
        + labor_bookings
    )

    # ========================================================
    # 17. BOOKINGS THIS MONTH
    # ========================================================

    current_year = datetime.now().year
    current_month = datetime.now().month

    bookings_this_month = 0

    # --------------------------------------------------------
    # Tractor bookings this month
    # --------------------------------------------------------

    tractor_monthly_data = (
        db.query(TractorBooking)
        .filter(
            TractorBooking.farmer_id == user_id
        )
        .all()
    )

    for booking in tractor_monthly_data:

        booking_date = getattr(
            booking,
            "booking_date",
            None,
        )

        if (
            hasattr(booking_date, "year")
            and booking_date.year == current_year
            and booking_date.month == current_month
        ):
            bookings_this_month += 1

    # --------------------------------------------------------
    # Labor bookings this month
    # --------------------------------------------------------

    labor_monthly_data = (
        db.query(LaborBooking)
        .filter(
            LaborBooking.farmer_id == user_id
        )
        .all()
    )

    for booking in labor_monthly_data:

        booking_date = getattr(
            booking,
            "booking_date",
            None,
        )

        if (
            hasattr(booking_date, "year")
            and booking_date.year == current_year
            and booking_date.month == current_month
        ):
            bookings_this_month += 1

    # --------------------------------------------------------
    # Seed purchases this month
    # --------------------------------------------------------

    seed_monthly_data = (
        db.query(SeedPurchase)
        .filter(
            SeedPurchase.buyer_id == user_id
        )
        .all()
    )

    for purchase in seed_monthly_data:

        purchase_date = getattr(
            purchase,
            "purchase_date",
            None,
        )

        if (
            hasattr(purchase_date, "year")
            and purchase_date.year == current_year
            and purchase_date.month == current_month
        ):
            bookings_this_month += 1

    # ========================================================
    # 18. MONTHLY BOOKING GRAPH
    # ========================================================

    booking_counter = defaultdict(int)

    # --------------------------------------------------------
    # Tractor bookings
    # --------------------------------------------------------

    for booking in tractor_monthly_data:

        month = _get_month_from_date(
            getattr(
                booking,
                "booking_date",
                None,
            )
        )

        if month:
            booking_counter[month] += 1

    # --------------------------------------------------------
    # Labor bookings
    # --------------------------------------------------------

    for booking in labor_monthly_data:

        month = _get_month_from_date(
            getattr(
                booking,
                "booking_date",
                None,
            )
        )

        if month:
            booking_counter[month] += 1

    # --------------------------------------------------------
    # Seed purchases
    # --------------------------------------------------------

    for purchase in seed_monthly_data:

        month = _get_month_from_date(
            getattr(
                purchase,
                "purchase_date",
                None,
            )
        )

        if month:
            booking_counter[month] += 1

    monthly_booking_graph = [
        {
            "month": month_abbr[index],
            "count": booking_counter[
                month_abbr[index]
            ],
        }
        for index in range(1, 13)
    ]

    # ========================================================
    # 19. MONTHLY INCOME / EXPENSE CHART
    # ========================================================

    monthly_income = defaultdict(float)
    monthly_expense = defaultdict(float)

    # --------------------------------------------------------
    # Payment income
    # --------------------------------------------------------

    completed_payments = (
        db.query(Payment)
        .filter(
            Payment.user_id == user_id,
            Payment.payment_status == "Completed",
        )
        .all()
    )

    for payment in completed_payments:

        payment_date = (
            getattr(
                payment,
                "created_at",
                None,
            )
            or getattr(
                payment,
                "payment_date",
                None,
            )
            or getattr(
                payment,
                "date",
                None,
            )
        )

        month = _get_month_from_date(
            payment_date
        )

        if month:

            monthly_income[month] += _safe_float(
                getattr(
                    payment,
                    "amount",
                    0,
                )
            )

    # --------------------------------------------------------
    # Seed expenses
    # --------------------------------------------------------

    for purchase in seed_monthly_data:

        month = _get_month_from_date(
            getattr(
                purchase,
                "purchase_date",
                None,
            )
        )

        if month:

            monthly_expense[month] += _safe_float(
                getattr(
                    purchase,
                    "total_price",
                    0,
                )
            )

    income_expense_chart = [
        {
            "month": month_abbr[index],
            "income": round(
                monthly_income[
                    month_abbr[index]
                ],
                2,
            ),
            "expense": round(
                monthly_expense[
                    month_abbr[index]
                ],
                2,
            ),
        }
        for index in range(1, 13)
    ]

    # ========================================================
    # 20. CROP PERFORMANCE
    # ========================================================

    crop_performance = []

    for crop in crops:

        crop_performance.append(
            {
                "crop": getattr(
                    crop,
                    "crop_name",
                    "Unknown Crop",
                ),
                "yield": _safe_float(
                    getattr(
                        crop,
                        "expected_yield",
                        0,
                    )
                ),
                "area": _safe_float(
                    getattr(
                        crop,
                        "area",
                        0,
                    )
                ),
            }
        )

    # ========================================================
    # 21. FINANCE CHART
    # ========================================================

    finance_chart = [
        {
            "name": "Income",
            "value": round(
                income,
                2,
            ),
        },
        {
            "name": "Expenses",
            "value": round(
                expenses,
                2,
            ),
        },
    ]

    # ========================================================
    # 22. PREMIUM CARDS
    # ========================================================

    premium_cards = [
        {
            "title": "AI Score",
            "value": ai_score,
            "color": "green",
        },
        {
            "title": "Crop Health",
            "value": crop_health_score,
            "color": "lime",
        },
        {
            "title": "Income",
            "value": income,
            "color": "blue",
        },
        {
            "title": "Profit",
            "value": profit,
            "color": "purple",
        },
    ]

    # ========================================================
    # 23. KPI CARDS
    # ========================================================

    kpi_cards = [
        {
            "title": "Total Crops",
            "value": total_crops,
            "icon": "🌱",
            "color": "#16a34a",
        },
        {
            "title": "Total Land",
            "value": total_land,
            "unit": "Acres",
            "icon": "🚜",
            "color": "#15803d",
        },
        {
            "title": "Bookings",
            "value": total_bookings,
            "icon": "📅",
            "color": "#2563eb",
        },
        {
            "title": "Profit",
            "value": profit,
            "icon": "💰",
            "color": "#9333ea",
        },
    ]

    # ========================================================
    # 24. RECENT ACTIVITIES
    # ========================================================

    recent_activities = []

    # --------------------------------------------------------
    # Tractor history
    # --------------------------------------------------------

    tractor_history = (
        db.query(
            TractorBooking,
            Tractor,
        )
        .join(
            Tractor,
            TractorBooking.tractor_id
            == Tractor.id,
        )
        .filter(
            TractorBooking.farmer_id
            == user_id
        )
        .order_by(
            desc(
                TractorBooking.id
            )
        )
        .limit(5)
        .all()
    )

    for booking, tractor in tractor_history:

        recent_activities.append(
            {
                "type": "tractor",
                "title": "Tractor Booking",
                "description": (
                    f"Booked "
                    f"{getattr(tractor, 'tractor_name', 'Tractor')}"
                ),
                "date": _safe_date_string(
                    getattr(
                        booking,
                        "booking_date",
                        None,
                    )
                ),
            }
        )

    # --------------------------------------------------------
    # Labor history
    # --------------------------------------------------------

    labor_history = (
        db.query(
            LaborBooking,
            Labor,
        )
        .join(
            Labor,
            LaborBooking.labor_id
            == Labor.id,
        )
        .filter(
            LaborBooking.farmer_id
            == user_id
        )
        .order_by(
            desc(
                LaborBooking.id
            )
        )
        .limit(5)
        .all()
    )

    for booking, labor in labor_history:

        recent_activities.append(
            {
                "type": "labor",
                "title": "Labor Booking",
                "description": (
                    f"Hired "
                    f"{getattr(labor, 'full_name', 'Labor')}"
                ),
                "date": _safe_date_string(
                    getattr(
                        booking,
                        "booking_date",
                        None,
                    )
                ),
            }
        )

    # --------------------------------------------------------
    # Seed purchase history
    # --------------------------------------------------------

    purchase_history = (
        db.query(
            SeedPurchase,
            Seed,
        )
        .join(
            Seed,
            SeedPurchase.seed_id
            == Seed.id,
        )
        .filter(
            SeedPurchase.buyer_id
            == user_id
        )
        .order_by(
            desc(
                SeedPurchase.id
            )
        )
        .limit(5)
        .all()
    )

    for purchase, seed in purchase_history:

        recent_activities.append(
            {
                "type": "seed",
                "title": "Seed Purchase",
                "description": (
                    f"Purchased "
                    f"{getattr(seed, 'seed_name', 'Seed')}"
                ),
                "date": _safe_date_string(
                    getattr(
                        purchase,
                        "purchase_date",
                        None,
                    )
                ),
            }
        )

    # --------------------------------------------------------
    # Sort recent activities
    # --------------------------------------------------------

    recent_activities = sorted(
        recent_activities,
        key=lambda item: item.get(
            "date",
            "",
        ),
        reverse=True,
    )[:10]

    # ========================================================
    # 25. WEATHER ANIMATION
    # ========================================================

    weather_animation = _get_weather_animation(
        temperature
    )

    # ========================================================
    # 26. AI HEALTH
    # ========================================================

    ai_health = {
        "score": ai_score,
        "status": _get_ai_health_status(
            ai_score
        ),
    }

    # ========================================================
    # 27. CROP SUMMARY
    # ========================================================

    if total_crops == 0:

        crop_summary = {
            "healthy": 0,
            "warning": 0,
            "critical": 0,
        }

    elif crop_health_score >= 80:

        crop_summary = {
            "healthy": total_crops,
            "warning": 0,
            "critical": 0,
        }

    elif crop_health_score >= 60:

        crop_summary = {
            "healthy": max(
                total_crops - 1,
                0,
            ),
            "warning": min(
                1,
                total_crops,
            ),
            "critical": 0,
        }

    else:

        crop_summary = {
            "healthy": 0,
            "warning": max(
                total_crops - 1,
                0,
            ),
            "critical": 1,
        }

    # ========================================================
    # 28. FARMER PROFILE CARD
    # ========================================================

    farmer_profile = {
        "name": farmer_name,
        "location": city,
        "profile_completion": profile_completion,
        "verified": True,
    }

    # ========================================================
    # 29. WEATHER SECTION
    # ========================================================

    weather_section = {
        "current": weather_card,
        "animation": weather_animation,
    }

    # ========================================================
    # 30. AI SECTION
    # ========================================================

    ai_section = {
        "score": ai_score,
        "health": ai_health,
        "recommendation": ai_tip,
    }

    # ========================================================
    # 31. CROP SECTION
    # ========================================================

    crop_section = {
        "summary": crop_summary,
        "performance": crop_performance,
        "health": {
            "health_score": crop_health_score,
            "health_status": crop_health_status,
            "disease_risk": disease_risk,
            "recommendation": crop_recommendation,
        },
    }

    # ========================================================
    # 32. FINANCE SECTION
    # ========================================================

    finance_section = {
        "income": income,
        "expenses": expenses,
        "profit": profit,
        "total_spending": total_spending,
        "chart": finance_chart,
        "monthly_chart": income_expense_chart,
    }

    # ========================================================
    # 33. ACTIVITY SECTION
    # ========================================================

    activity_section = {
        "recent": recent_activities,
        "monthly_graph": monthly_booking_graph,
    }

    # ========================================================
    # 34. DASHBOARD SUMMARY
    # ========================================================

    dashboard_summary = {
        "total_bookings": total_bookings,
        "income": income,
        "expenses": expenses,
        "profit": profit,
        "crop_health": crop_health_score,
        "ai_score": ai_score,
        "profile_completion": profile_completion,
        "notifications": notification_count,
    }

    # ========================================================
    # 35. DASHBOARD ANALYTICS
    # ========================================================

    dashboard_analytics = {
        "income": income,
        "expenses": expenses,
        "profit": profit,
        "total_bookings": total_bookings,
        "tractor_bookings": tractor_bookings,
        "labor_bookings": labor_bookings,
        "seed_purchases": seed_purchases,
    }

    # ========================================================
    # 36. DASHBOARD VERSION
    # ========================================================

    dashboard_version = {
        "name": "FarmBuddy AI Premium Dashboard",
        "version": "3.0",
        "build": "Lesson-31",
        "environment": "Production",
    }

    # ========================================================
    # 37. QUICK ACTIONS
    # ========================================================

    quick_actions = [
        {
            "title": "Book Tractor",
            "route": "/tractors",
            "icon": "🚜",
        },
        {
            "title": "Hire Labor",
            "route": "/labors",
            "icon": "👨‍🌾",
        },
        {
            "title": "Buy Seeds",
            "route": "/seeds",
            "icon": "🌱",
        },
        {
            "title": "AI Disease Detection",
            "route": "/disease-detection",
            "icon": "🤖",
        },
    ]

    # ========================================================
    # 38. NOTIFICATIONS
    # ========================================================

    notifications = [
        {
            "type": "booking",
            "message": (
                f"You have "
                f"{tractor_bookings} tractor bookings."
            ),
        },
        {
            "type": "weather",
            "message": (
                f"Today's weather is "
                f"{weather_status}."
            ),
        },
        {
            "type": "crop",
            "message": (
                f"{total_crops} crops "
                f"are currently active."
            ),
        },
    ]

    # ========================================================
    # 39. FINAL RESPONSE
    # ========================================================
    #
    # IMPORTANT:
    # crop_health MUST be an integer because
    # DashboardResponse declares:
    #
    #     crop_health: int
    #
    # Detailed crop-health information is returned through:
    #
    #     crop_health_score
    #     crop_health_status
    #     disease_risk
    #     crop_recommendation
    #
    # ========================================================

    return {
        # ----------------------------------------------------
        # Required DashboardResponse fields
        # ----------------------------------------------------

        "farmer_name": farmer_name,

        "total_crops": total_crops,
        "total_land": total_land,
        "active_crops": active_crops,

        "weather_status": weather_status,

        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "city": city,
        "updated_at": updated_at,

        "current_date": current_date,
        "location": city,
        "verified": True,

        "market_price": "Coming Soon",
        "ai_tip": ai_tip,

        "total_bookings": total_bookings,
        "tractor_bookings": tractor_bookings,
        "labor_bookings": labor_bookings,
        "seed_purchases": seed_purchases,

        "total_spending": total_spending,

        "profile_completion": profile_completion,

        "notification_count": notification_count,

        "monthly_booking_graph": monthly_booking_graph,

        "bookings_this_month": bookings_this_month,

        "income": income,
        "expenses": expenses,

        # IMPORTANT: integer, NOT dictionary
        "crop_health": crop_health_score,

        "ai_score": ai_score,

        "recent_activities": recent_activities,

        "crop_health_score": crop_health_score,

        "crop_health_status": crop_health_status,

        "disease_risk": disease_risk,

        "crop_recommendation": crop_recommendation,

        "weather": weather_card,

        # ----------------------------------------------------
        # Additional dashboard data
        # ----------------------------------------------------

        "weather_animation": weather_animation,

        "weather_section": weather_section,

        "farmer_profile": farmer_profile,

        "ai_health": ai_health,

        "ai_section": ai_section,

        "crop_summary": crop_summary,

        "crop_performance": crop_performance,

        "crop_section": crop_section,

        "finance_chart": finance_chart,

        "income_expense_chart": income_expense_chart,

        "finance_section": finance_section,

        "activity_section": activity_section,

        "dashboard_summary": dashboard_summary,

        "dashboard_analytics": dashboard_analytics,

        "dashboard_version": dashboard_version,

        "premium_cards": premium_cards,

        "kpi_cards": kpi_cards,

        "farmer_news": FARMER_NEWS,

        "notifications": notifications,

        "quick_actions": quick_actions,
    }