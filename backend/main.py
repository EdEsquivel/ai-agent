from fastapi import Depends, FastAPI
from fastapi.responses import StreamingResponse

from backend.schemas import ChatRequest
from backend.services.ai_service import AIService
from backend.services.ollama_service import OllamaService


app = FastAPI()


def get_ai_service() -> AIService:
    return OllamaService()


@app.get("/")
def root():
    return {
        "message": "AI Agent Service is running successfully!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(
    request: ChatRequest,
    ai_service: AIService = Depends(get_ai_service)
):

    response = ai_service.generate_response(request.message)

    return {
        "response": response
    }

@app.post("/chat/stream")
def chat_stream(
    request: ChatRequest,
    ai_service: AIService = Depends(get_ai_service)
):
    return StreamingResponse(
        ai_service.generate_response_stream(request.message),
        media_type="text/plain"
    )