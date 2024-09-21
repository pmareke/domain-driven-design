import uuid

from weather_app.weather.domain.command import Command
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.command_response import CommandResponse


class DeleteOneWeatherCommand(Command):

    def __init__(self, weather_id: str) -> None:
        self.weather_id = weather_id
        super().__init__(uuid.uuid1())


class DeleteOneWeatherCommandResponse(CommandResponse):
    pass


class DeleteOneWeatherCommandHandler(CommandHandler):

    def __init__(self, repository: WeatherRepository):
        self.repository = repository

    def process(
        self, command: DeleteOneWeatherCommand
    ) -> DeleteOneWeatherCommandResponse:
        self.repository.delete(command.weather_id)
        return DeleteOneWeatherCommandResponse()
