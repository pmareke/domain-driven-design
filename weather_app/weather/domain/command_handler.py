from abc import ABC, abstractmethod
from weather.domain.command import Command
from typing import Any


class CommandHandler(ABC):
    @abstractmethod
    def process(self, command: Command) -> Any:
        pass
