from collections.abc import AsyncIterator

from ollama import AsyncClient, Client

from backend.config import settings
from backend.services.ai_service import AIService


class OllamaService(AIService):

    def __init__(self):
        self.client = Client(host=settings.ollama_host)
        self.async_client = AsyncClient(host=settings.ollama_host)


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

    async def generate_response_stream(
        self,
        message: str
    ) -> AsyncIterator[str]:

            response = await self.async_client.chat(
                model=settings.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                stream=True
            )

            async for chunk in response:
                yield chunk["message"]["content"]
