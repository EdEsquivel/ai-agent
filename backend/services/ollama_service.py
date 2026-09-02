from ollama import Client

from backend.config import settings
from backend.services.ai_service import AIService


class OllamaService(AIService):

    def __init__(self):
        self.client = Client(host=settings.ollama_host)

    def generate_response(self, message: str) -> str:
        response = self.client.chat(
            model=settings.model_name,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response["message"]["content"]