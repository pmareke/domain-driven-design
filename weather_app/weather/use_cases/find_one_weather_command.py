import uuid

from weather_app.weather.domain.command import Command
from weather_app.weather.domain.weather import Weather, WeatherNotFoundException
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.command_response import CommandResponse


class FindOneWeatherCommand(Command):
    def __init__(self, weather_id: str) -> None:
        self.weather_id = weather_id
        super().__init__(uuid.uuid1())


class FindOneWeatherCommandResponse(CommandResponse):
    def __init__(self, weather: Weather) -> None:
        self.weather = weather


class FindOneWeatherCommandHandler(CommandHandler):
    def __init__(self, repository: WeatherRepository):
        self.repository = repository

    def process(
        self, command: FindOneWeatherCommand
    ) -> FindOneWeatherCommandResponse:
        weather = self.repository.find(command.weather_id)
        if not weather:
            raise WeatherNotFoundException()
        return FindOneWeatherCommandResponse(weather)
