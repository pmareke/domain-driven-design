import uuid

from weather.domain.command import Command
from weather.domain.weather import Weather
from weather.domain.command_handler import CommandHandler
from weather.domain.weather_repository import WeatherRepository


class FindOneWeatherCommand(Command):
    def __init__(self, city_id: int) -> None:
        self.city_id = city_id
        super().__init__(uuid.uuid1())


class FindOneWeatherCommandHandler(CommandHandler):
    def __init__(self, repository: WeatherRepository):
        self.repository = repository

    def process(self, command: FindOneWeatherCommand) -> Weather:
        return self.repository.find(command.city_id)
