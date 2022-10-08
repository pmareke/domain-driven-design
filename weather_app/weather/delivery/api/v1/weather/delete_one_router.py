from fastapi import APIRouter, Depends
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.use_cases.delete_one_weather_command import DeleteOneWeatherCommand, DeleteOneWeatherCommandHandler
from weather_app.weather.infrastructure.pymongo_weather_repository import PyMongoWeatherRepository

delete_one_router = APIRouter()


async def _delete_one_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return DeleteOneWeatherCommandHandler(repository)


@delete_one_router.delete("/api/v1/weather/{city_id}")
def delete_weather(
    city_id: str,
    handler: CommandHandler = Depends(_delete_one_command_handler)
) -> None:
    command = DeleteOneWeatherCommand(city_id)
    handler.process(command)
