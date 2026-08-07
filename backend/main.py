from fastapi import FastAPI
from backend.schemas import ChatRequest

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

    return {
        "response": f"Received message: {request.message}"
    }