from typing import List, Dict

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi import status
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather import Weather, WeatherNotFoundException, WeatherDTO
from weather_app.weather.use_cases.find_all_weathers_command import FindAllWeathersCommand, FindAllWeathersCommandHandler
from weather_app.weather.use_cases.find_one_weather_command import FindOneWeatherCommand, FindOneWeatherCommandHandler
from weather_app.weather.use_cases.create_one_weather_command import CreateOneWeatherCommand, CreateOneWeatherCommandHandler
from weather_app.weather.use_cases.delete_one_weather_command import DeleteOneWeatherCommand, DeleteOneWeatherCommandHandler
from weather_app.weather.infrastructure.pymongo_weather_repository import PyMongoWeatherRepository

router = APIRouter()


@router.get("/health")
def health() -> Dict[str, bool]:
    return {"ok": True}


async def _find_all_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return FindAllWeathersCommandHandler(repository)


@router.get("/api/v1/weather")
def find_all_weathers(
    handler: CommandHandler = Depends(_find_all_command_handler)
) -> Dict[str, List[Weather]]:
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


async def _create_one_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return CreateOneWeatherCommandHandler(repository)


@router.post("/api/v1/weather")
def create_weather(
    weather: WeatherDTO,
    response: Response,
    handler: CommandHandler = Depends(_create_one_command_handler)
) -> Dict:
    command = CreateOneWeatherCommand(weather)
    weather_response = handler.process(command)
    response.status_code = status.HTTP_201_CREATED
    return {"id": weather_response.weather_id}


async def _delete_one_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return DeleteOneWeatherCommandHandler(repository)


@router.delete("/api/v1/weather/{city_id}")
def delete_weather(
    city_id: str,
    handler: CommandHandler = Depends(_delete_one_command_handler)
) -> None:
    command = DeleteOneWeatherCommand(city_id)
    handler.process(command)
