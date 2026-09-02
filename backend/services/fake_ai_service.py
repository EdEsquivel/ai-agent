from collections.abc import AsyncIterator

from backend.services.ai_service import AIService


class FakeAIService(AIService):

    def generate_response(self, message: str) -> str:
        return f"FAKE RESPONSE: I received your message: '{message}'"

    async def generate_response_stream(
        self,
        message: str
    ) -> AsyncIterator[str]:

        response = f"FAKE RESPONSE: I received your message: '{message}'"

        for word in response.split():
            yield word + " "