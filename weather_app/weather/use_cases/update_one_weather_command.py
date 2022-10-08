import uuid

from weather_app.weather.domain.command import Command
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.command_response import CommandResponse
from weather_app.weather.domain.weather import WeatherDTO, Weather, WeatherNotFoundException


class UpdateOneWeatherCommand(Command):
    def __init__(self, weather_id: str, weather_dto: WeatherDTO) -> None:
        self.weather_id = weather_id
        self.weather_dto = weather_dto
        super().__init__(uuid.uuid1())


class UpdateOneWeatherCommandResponse(CommandResponse):
    def __init__(self, weather: Weather) -> None:
        self.weather = weather


class UpdateOneWeatherCommandHandler(CommandHandler):
    def __init__(self, repository: WeatherRepository):
        self.repository = repository

    def process(
        self, command: UpdateOneWeatherCommand
    ) -> UpdateOneWeatherCommandResponse:
        weather = self.repository.update(
            command.weather_id, command.weather_dto
        )
        if not weather:
            raise WeatherNotFoundException()
        return UpdateOneWeatherCommandResponse(weather)
