from collections.abc import Iterator

from backend.services.ai_service import AIService


class FakeAIService(AIService):

    def generate_response(self, message: str) -> str:
        return f"FAKE RESPONSE: I received your message: '{message}'"

    def generate_response_stream(self, message: str) -> Iterator[str]:
        response = f"FAKE RESPONSE: I received your message: '{message}'"

        for word in response.split():
            yield word + " "