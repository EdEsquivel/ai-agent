import asyncio

from backend.services.ai_service import AIService
from backend.services.concurrency_limited_ai_service import (
    ConcurrencyLimitedAIService
)


class SlowFakeAIService(AIService):

    def __init__(self):
        self.active_requests = 0
        self.max_active_requests = 0

    def generate_response(self, message: str) -> str:
        return "fake response"

    async def generate_response_stream(self, message: str):

        self.active_requests += 1

        self.max_active_requests = max(
            self.max_active_requests,
            self.active_requests
        )

        await asyncio.sleep(0.1)

        self.active_requests -= 1

        yield "fake response"


def test_concurrency_limit():

    async def run_test():

        fake_service = SlowFakeAIService()

        service = ConcurrencyLimitedAIService(
            fake_service,
            max_concurrent_requests=2
        )

        async def consume():
            async for _ in service.generate_response_stream("Hello"):
                pass

        await asyncio.gather(
            consume(),
            consume(),
            consume(),
        )

        assert fake_service.max_active_requests == 2

    asyncio.run(run_test())