from abc import ABC, abstractmethod
from weather_app.weather.domain.command import Command

from weather_app.weather.domain.command_response import CommandResponse


class CommandHandler(ABC):
    @abstractmethod
    def process(self, command: Command) -> CommandResponse:
        pass
