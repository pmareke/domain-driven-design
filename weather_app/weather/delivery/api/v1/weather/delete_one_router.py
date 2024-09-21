from fastapi import APIRouter, Depends, status
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.use_cases.delete_one_weather_command import (
    DeleteOneWeatherCommand,
    DeleteOneWeatherCommandHandler,
)
from weather_app.weather.infrastructure.pymongo_weather_repository import (
    PyMongoWeatherRepository,
)

delete_one_router = APIRouter()


async def _delete_one_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return DeleteOneWeatherCommandHandler(repository)


@delete_one_router.delete(
    "/api/v1/weather/{weather_id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete_weather(
    weather_id: str, handler: CommandHandler = Depends(_delete_one_command_handler)
) -> None:
    command = DeleteOneWeatherCommand(weather_id)
    handler.process(command)
