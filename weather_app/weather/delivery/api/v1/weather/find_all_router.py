from typing import List, Dict

from fastapi import APIRouter, Depends
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather import Weather
from weather_app.weather.use_cases.find_all_weathers_command import FindAllWeathersCommand, FindAllWeathersCommandHandler
from weather_app.weather.infrastructure.pymongo_weather_repository import PyMongoWeatherRepository
from weather_app.weather.delivery.api.v1.weather.weather_list_response import WeatherListResponse

find_all_router = APIRouter()


async def _find_all_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return FindAllWeathersCommandHandler(repository)


@find_all_router.get("/api/v1/weather", response_model=WeatherListResponse)
def find_all_weathers(
    handler: CommandHandler = Depends(_find_all_command_handler)
) -> Dict[str, List[Weather]]:
    command = FindAllWeathersCommand()
    weathers_response = handler.process(command)
    return {"weathers": weathers_response.weathers}
