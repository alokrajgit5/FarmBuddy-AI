import random

from app.ai.labels.classes import CLASSES


def detect_disease():

    disease = random.choice(CLASSES)

    treatments = {

        "Healthy": (
            "No treatment required.",
            "Continue regular monitoring."
        ),

        "Leaf Blight": (
            "Spray Copper Oxychloride.",
            "Avoid excess irrigation."
        ),

        "Powdery Mildew": (
            "Use Sulfur Fungicide.",
            "Maintain proper airflow."
        ),

        "Rust Disease": (
            "Apply Mancozeb Spray.",
            "Remove infected leaves."
        ),

        "Bacterial Spot": (
            "Use Copper Spray.",
            "Avoid water splashing."
        ),

        "Early Blight": (
            "Apply Chlorothalonil.",
            "Remove infected leaves."
        ),

        "Late Blight": (
            "Use Metalaxyl Fungicide.",
            "Avoid overwatering."
        )

    }

    treatment, prevention = treatments[disease]

    confidence = round(
        random.uniform(90, 99.9),
        2
    )

    return {

        "disease": disease,

        "confidence": confidence,

        "treatment": treatment,

        "prevention": prevention

    }