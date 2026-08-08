from fastapi import FastAPI
from backend.schemas import ChatRequest
from ollama import chat as ollama_chat

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

    response = ollama_chat(
        model="gemma4:12b",
        messages=[
            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    return {
        "response": response["message"]["content"]
    }