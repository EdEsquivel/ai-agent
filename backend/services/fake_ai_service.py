from collections.abc import AsyncIterator

from backend.services.ai_service import AIService


class FakeAIService(AIService):

    async def generate_response(
        self,
        message: str
    ) -> str:
        return f"FAKE RESPONSE: I received your message: '{message}'"

    async def generate_response_stream(
        self,
        message: str
    ) -> AsyncIterator[str]:
        yield f"FAKE RESPONSE: I received your message: '{message}'"