from typing import List
from weather.domain.command import Command
from weather.domain.weather import Weather
from weather.domain.command_handler import CommandHandler
from weather.domain.weather_repository import WeatherRepository


class FindAllWeathersCommand(Command):
    pass


class FindAllWeathersCommandHandler(CommandHandler):
    def __init__(self, repository: WeatherRepository):
        self.repository = repository

    def process(self, _command: FindAllWeathersCommand) -> List[Weather]:
        return self.repository.find_all()
