from app.schemas.scheme_schema import SchemeRequest


def recommend_scheme(data: SchemeRequest):

    recommendations = []

    state = data.state.lower()
    crop = data.crop.lower()
    land = data.land_size

    if land <= 5:
        recommendations.append({

            "scheme_name": "PM-KISAN",

            "eligibility": "Eligible",

            "eligibility_reason": "Land holding is within the eligible limit.",

            "benefit": "₹6000 annual financial support",

            "subsidy": "₹6000/Year",

            "application_mode": "Online",

            "documents_required": [
                "Aadhaar Card",
                "Bank Passbook",
                "Land Record"
            ],

            "official_portal": "https://pmkisan.gov.in",

            "approval_time": "15-30 Days",

            "last_date": "Open Throughout the Year",

            "important_note": "Ensure Aadhaar and bank account are linked."

        })

    if crop in [
        "rice",
        "wheat",
        "maize",
        "cotton"
    ]:

        recommendations.append({

            "scheme_name": "PM Fasal Bima Yojana",

            "eligibility": "Eligible",

            "eligibility_reason": "Selected crop is covered under PMFBY.",

            "benefit": "Crop Insurance",

            "subsidy": "Premium Subsidy",

            "application_mode": "Online / CSC",

            "documents_required": [
                "Aadhaar Card",
                "Land Record",
                "Bank Account"
            ],

            "official_portal": "https://pmfby.gov.in",

            "approval_time": "15 Days",

            "last_date": "Before Sowing Season",

            "important_note": "Apply before the crop season begins."

        })

    if state in [
        "bihar",
        "uttar pradesh",
        "madhya pradesh",
        "jharkhand"
    ]:

        recommendations.append({

            "scheme_name": "Soil Health Card Scheme",

            "eligibility": "Eligible",

            "eligibility_reason": "State supports Soil Health Card implementation.",

            "benefit": "Free Soil Testing",

            "subsidy": "100% Government Support",

            "application_mode": "Agriculture Office",

            "documents_required": [
                "Aadhaar Card",
                "Land Record"
            ],

            "official_portal": "https://soilhealth.dac.gov.in",

            "approval_time": "7-15 Days",

            "last_date": "Open Throughout the Year",

            "important_note": "Carry a fresh soil sample while applying."

        })

    if crop in [
        "tomato",
        "potato",
        "vegetables"
    ]:

        recommendations.append({

            "scheme_name": "PM Krishi Sinchai Yojana",

            "eligibility": "Eligible",

            "eligibility_reason": "Suitable for horticulture and irrigated crops.",

            "benefit": "Micro Irrigation Subsidy",

            "subsidy": "Up to 55%",

            "application_mode": "Online",

            "documents_required": [
                "Aadhaar Card",
                "Land Record",
                "Bank Passbook"
            ],

            "official_portal": "https://pmksy.gov.in",

            "approval_time": "30-45 Days",

            "last_date": "As per State Notification",

            "important_note": "Subsidy percentage may differ by state."

        })

    recommendations.append({

        "scheme_name": "Kisan Credit Card",

        "eligibility": "Eligible",

        "eligibility_reason": "Available for most eligible farmers.",

        "benefit": "Low Interest Agricultural Loan",

        "subsidy": "Interest Subsidy",

        "application_mode": "Bank Branch / Online",

        "documents_required": [
            "Aadhaar Card",
            "PAN Card",
            "Bank Passbook",
            "Land Record"
        ],

        "official_portal": "https://www.myscheme.gov.in",

        "approval_time": "7-20 Days",

        "last_date": "Open Throughout the Year",

        "important_note": "Keep KYC documents updated."

    })

    return {
        "recommendations": recommendations[:3]
    }