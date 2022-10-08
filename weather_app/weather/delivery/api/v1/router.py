from typing import List, Dict

from fastapi import APIRouter, Depends
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather import Weather
from weather_app.weather.use_cases.find_all_weathers_command import FindAllWeathersCommand, FindAllWeathersCommandHandler
from weather_app.weather.use_cases.find_one_weather_command import FindOneWeatherCommand, FindOneWeatherCommandHandler
from weather_app.weather.infrastructure.pymongo_weather_repository import PyMongoWeatherRepository

router = APIRouter()


@router.get("/health")
def health() -> Dict[str, bool]:
    return {"ok": True}


async def _find_all_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return FindAllWeathersCommandHandler(repository)


@router.get("/api/v1/weather")
def find_all_weathers(handler: CommandHandler = Depends(_find_all_command_handler)) -> Dict[str, List[Weather]]:
    command = FindAllWeathersCommand()
    weathers_response = handler.process(command)
    return {"weathers": weathers_response.weathers}


async def _find_one_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return FindOneWeatherCommandHandler(repository)


@router.get("/api/v1/weather/{city_id}")
def find_weather(
    city_id: str, handler: CommandHandler = Depends(_find_one_command_handler)
) -> Weather:
    command = FindOneWeatherCommand(city_id)
    weather_response = handler.process(command)
    weather: Weather = weather_response.weather
    return weather
