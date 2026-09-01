from backend.services.ai_service import AIService


class FakeAIService(AIService):

    def generate_response(self, message: str) -> str:
        return f"FAKE RESPONSE: I received your message: '{message}'"