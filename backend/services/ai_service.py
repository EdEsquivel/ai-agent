from abc import ABC, abstractmethod
from collections.abc import AsyncIterator


class AIService(ABC):

    @abstractmethod
    def generate_response(self, message: str) -> str:
        pass

    @abstractmethod
    async def generate_response_stream(
        self,
        message: str
    ) -> AsyncIterator[str]:
        pass