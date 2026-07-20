from fastapi import FastAPI

app = FastAPI(
    title="FarmBuddy AI",
    description="AI Powered Smart Agriculture Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "FarmBuddy AI",
        "status": "Running Successfully 🚜",
        "version": "1.0.0"
    }