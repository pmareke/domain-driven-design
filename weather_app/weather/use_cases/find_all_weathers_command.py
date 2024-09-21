import uuid
from typing import List
from weather_app.weather.domain.command import Command
from weather_app.weather.domain.weather import Weather
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.command_response import CommandResponse


class FindAllWeathersCommand(Command):

    def __init__(self) -> None:
        super().__init__(uuid.uuid1())


class FindAllWeathersCommandResponse(CommandResponse):

    def __init__(self, weathers: List[Weather]) -> None:
        self.weathers = weathers


class FindAllWeathersCommandHandler(CommandHandler):

    def __init__(self, repository: WeatherRepository):
        self.repository = repository

    def process(
        self, _command: FindAllWeathersCommand
    ) -> "FindAllWeathersCommandResponse":
        weathers: List[Weather] = self.repository.find_all()
        return FindAllWeathersCommandResponse(weathers)
