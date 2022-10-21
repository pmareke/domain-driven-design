import uuid

from weather_app.weather.domain.command import Command
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.command_response import CommandResponse
from weather_app.weather.domain.weather import WeatherFactory


class CreateOneWeatherCommand(Command):

    def __init__(self, weather_id: str, temperature: int, city: str) -> None:
        self.weather_id = weather_id
        self.temperature = temperature
        self.city = city
        super().__init__(uuid.uuid1())


class CreateOneWeatherCommandResponse(CommandResponse):
    pass


class CreateOneWeatherCommandHandler(CommandHandler):

    def __init__(self, repository: WeatherRepository):
        self.repository = repository

    def process(
            self, command: CreateOneWeatherCommand
    ) -> CreateOneWeatherCommandResponse:
        weather = WeatherFactory.make(command.weather_id, command.temperature,
                                      command.city)
        self.repository.save(weather)
        return CreateOneWeatherCommandResponse()
