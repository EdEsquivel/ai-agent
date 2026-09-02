from abc import ABC, abstractmethod
from collections.abc import Iterator


class AIService(ABC):

    @abstractmethod
    def generate_response(self, message: str) -> str:
        pass

    @abstractmethod
    def generate_response_stream(self, message: str) -> Iterator[str]:
        pass