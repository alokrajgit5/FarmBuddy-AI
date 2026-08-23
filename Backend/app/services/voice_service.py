import os
import speech_recognition as sr

from fastapi import UploadFile
from langdetect import detect

from gtts import gTTS
from fastapi.responses import FileResponse

from app.services.chat_service import (
    get_chat_response
)

from app.schemas.chat_schema import (
    ChatRequest
)


def speech_to_text(file: UploadFile):

    os.makedirs("audio", exist_ok=True)

    audio_path = os.path.join(
        "audio",
        file.filename
    )

    with open(audio_path, "wb") as buffer:
        buffer.write(file.file.read())

    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        return "Could not understand audio."

    except sr.RequestError:
        return "Speech service unavailable."


def text_to_speech(text: str):

    os.makedirs("audio", exist_ok=True)

    output_path = os.path.join(
        "audio",
        "output.mp3"
    )

    try:
        language = detect(text)
    except:
        language = "en"

    if language not in [
        "en",
        "hi"
    ]:
        language = "en"

    tts = gTTS(
        text=text,
        lang=language
    )

    tts.save(output_path)

    return output_path
def ask_ai_from_voice(
    file: UploadFile
):

    question = speech_to_text(file)

    if (
        question == "Could not understand audio."
        or
        question == "Speech service unavailable."
    ):
        return {
            "question": question,
            "answer": None
        }

    response = get_chat_response(
        ChatRequest(
            question=question
        )
    )

    return {
        "question": question,
        "answer": response["answer"]
    }
def ask_ai_with_voice(file: UploadFile):

    result = ask_ai_from_voice(file)

    if result["answer"] is None:
        return None

    audio_path = text_to_speech(
        result["answer"]
    )

    return audio_path