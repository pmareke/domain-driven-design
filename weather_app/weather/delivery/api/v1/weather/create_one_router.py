from typing import Dict

from fastapi import APIRouter, Depends, Response
from fastapi import status
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather import WeatherDTO
from weather_app.weather.use_cases.create_one_weather_command import CreateOneWeatherCommand, CreateOneWeatherCommandHandler
from weather_app.weather.infrastructure.pymongo_weather_repository import PyMongoWeatherRepository

create_one_router = APIRouter()


async def _create_one_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return CreateOneWeatherCommandHandler(repository)


@create_one_router.post("/api/v1/weather")
def create_weather(
    weather: WeatherDTO,
    response: Response,
    handler: CommandHandler = Depends(_create_one_command_handler)
) -> Dict:
    command = CreateOneWeatherCommand(weather)
    weather_response = handler.process(command)
    response.status_code = status.HTTP_201_CREATED
    return {"id": weather_response.weather_id}
