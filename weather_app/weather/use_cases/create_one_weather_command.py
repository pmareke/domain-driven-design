import uuid

from weather_app.weather.domain.command import Command
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.command_response import CommandResponse
from weather_app.weather.domain.weather import Weather


class CreateOneWeatherCommand(Command):
    def __init__(self, temperature: int, city: str) -> None:
        self.temperature = temperature
        self.city = city
        super().__init__(uuid.uuid1())


class CreateOneWeatherCommandResponse(CommandResponse):
    def __init__(self, weather_id: str) -> None:
        self.weather_id = weather_id


class CreateOneWeatherCommandHandler(CommandHandler):
    def __init__(self, repository: WeatherRepository):
        self.repository = repository

    def process(
        self, command: CreateOneWeatherCommand
    ) -> CreateOneWeatherCommandResponse:
        weather = Weather(command.temperature, command.city)
        weather_id = self.repository.save(weather)
        return CreateOneWeatherCommandResponse(weather_id)
