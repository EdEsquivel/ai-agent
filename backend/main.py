from fastapi import FastAPI
from backend.schemas import ChatRequest
from backend.services.ollama_service import generate_response

app = FastAPI()


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
def chat(request: ChatRequest):

    response = generate_response(request.message)

    return {
        "response": response
    }