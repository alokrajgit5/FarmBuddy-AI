from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from fastapi.responses import FileResponse

from app.services.voice_service import (
    speech_to_text,
    ask_ai_from_voice,
    ask_ai_with_voice
)

router = APIRouter(
    prefix="/api/voice",
    tags=["Voice AI"]
)


@router.post("/speech-to-text")
def convert_speech_to_text(
    file: UploadFile = File(...)
):

    text = speech_to_text(file)

    return {
        "text": text
    }


@router.post("/ask-ai")
def ask_ai(
    file: UploadFile = File(...)
):

    return ask_ai_from_voice(file)


@router.post("/ask-ai-voice")
def ask_ai_voice(
    file: UploadFile = File(...)
):

    audio_path = ask_ai_with_voice(file)

    if audio_path is None:
        return {
            "message": "Could not process audio."
        }

    return FileResponse(
        audio_path,
        media_type="audio/mpeg",
        filename="response.mp3"
    )