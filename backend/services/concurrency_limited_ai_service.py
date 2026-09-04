import asyncio
from collections.abc import AsyncIterator

from backend.services.ai_service import AIService


class ConcurrencyLimitedAIService(AIService):

    def __init__(
        self,
        service: AIService,
        max_concurrent_requests: int
    ):
        self.service = service
        self.semaphore = asyncio.Semaphore(
            max_concurrent_requests
        )

    async def generate_response(
        self,
        message: str
    ) -> str:

        async with self.semaphore:

            return await self.service.generate_response(
                message
            )

    async def generate_response_stream(
        self,
        message: str
    ) -> AsyncIterator[str]:

        async with self.semaphore:

            async for chunk in self.service.generate_response_stream(
                message
            ):
                yield chunk