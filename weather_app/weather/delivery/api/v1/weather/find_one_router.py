from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather import Weather, WeatherNotFoundException
from weather_app.weather.use_cases.find_one_weather_command import (
    FindOneWeatherCommand,
    FindOneWeatherCommandHandler,
)

from weather_app.weather.infrastructure.pymongo_weather_repository import (
    PyMongoWeatherRepository,
)
from weather_app.weather.delivery.api.v1.weather.weather_response import WeatherResponse

find_one_router = APIRouter()


async def _find_one_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return FindOneWeatherCommandHandler(repository)


@find_one_router.get("/api/v1/weather/{weather_id}", response_model=WeatherResponse)
def find_weather(
    weather_id: str,
    handler: FindOneWeatherCommandHandler = Depends(_find_one_command_handler),
) -> WeatherResponse:
    try:
        command = FindOneWeatherCommand(weather_id)
        weather_response = handler.process(command)
    except WeatherNotFoundException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Weather {weather_id} not found",
        ) from exception

    response = WeatherResponse(
        weather_id=weather_response.weather.weather_id,
        temperature=weather_response.weather.temperature,
        city=weather_response.weather.city,
    )
    return response
