from google import genai

from app.core.config import settings
from app.schemas.chat_schema import ChatRequest

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def get_chat_response(data: ChatRequest):

    system_prompt = """
You are FarmBuddy AI.

Rules:
- Answer only agriculture-related questions.
- Reply only about agriculture.
- Reply in the SAME language as the farmer.
- Keep answers short and practical.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"""
{system_prompt}

Farmer Question:
{data.question}
"""
        )

        return {
            "question": data.question,
            "answer": response.text
        }

    except Exception as e:

        print("\n========== GEMINI ERROR ==========")

        print(type(e))

        print(e)
        print("==================================\n")

        return {
            "question": data.question,
            "answer": str(e)
        }