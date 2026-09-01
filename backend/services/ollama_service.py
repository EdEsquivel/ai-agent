from ollama import chat

from backend.services.ai_service import AIService


MODEL_NAME = "gemma4:12b"


class OllamaService(AIService):

    def generate_response(self, message: str) -> str:
        response = chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response["message"]["content"]