import uuid

from weather_app.weather.domain.command import Command
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.command_response import CommandResponse
from weather_app.weather.domain.weather import WeatherDTO


class CreateOneWeatherCommand(Command):
    def __init__(self, weather: WeatherDTO) -> None:
        self.weather = weather
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
        weather_id = self.repository.save(command.weather)
        return CreateOneWeatherCommandResponse(weather_id)
