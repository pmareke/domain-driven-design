from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather import Weather, WeatherNotFoundException
from weather_app.weather.use_cases.find_one_weather_command import FindOneWeatherCommand, FindOneWeatherCommandHandler
from weather_app.weather.infrastructure.pymongo_weather_repository import PyMongoWeatherRepository

find_one_router = APIRouter()


async def _find_one_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return FindOneWeatherCommandHandler(repository)


@find_one_router.get("/api/v1/weather/{city_id}")
def find_weather(
    city_id: str, handler: CommandHandler = Depends(_find_one_command_handler)
) -> Weather:
    try:
        command = FindOneWeatherCommand(city_id)
        weather_response = handler.process(command)
    except WeatherNotFoundException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Weather {city_id} not found"
        ) from exception

    weather: Weather = weather_response.weather
    return weather
