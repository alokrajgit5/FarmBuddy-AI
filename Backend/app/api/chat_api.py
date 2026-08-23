from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user

from app.schemas.chat_schema import (
    ChatRequest,
    ChatResponse
)

from app.services.chat_service import (
    get_chat_response
)

router = APIRouter(
    prefix="/api/chat",
    tags=["AI Chatbot"]
)


@router.post(
    "/",
    response_model=ChatResponse
)
def chat(
    data: ChatRequest,
    current_user=Depends(get_current_user)
):
    return get_chat_response(data)