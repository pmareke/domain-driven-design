from fastapi import APIRouter, Depends
from weather.domain.command_handler import CommandHandler
from weather.domain.weather_repository import WeatherRepository
from weather.use_cases.find_all_weathers_command import FindAllWeathersCommand, FindAllWeathersCommandHandler
from weather.use_cases.find_one_weather_command import FindOneWeatherCommand, FindOneWeatherCommandHandler
from weather.infrastructure.in_memory_weather_repository import InMemoryWeatherRepository

router = APIRouter()


@router.get("/health")
def health():
    return {"ok": True}


async def find_all_command_handler() -> CommandHandler:
    repository = InMemoryWeatherRepository()
    return FindAllWeathersCommandHandler(repository)


async def find_one_command_handler() -> CommandHandler:
    repository = InMemoryWeatherRepository()
    return FindOneWeatherCommandHandler(repository)


@router.get("/api/v1/weather")
def weather(handler: CommandHandler = Depends(find_all_command_handler)):
    command = FindAllWeathersCommand()
    return {"weathers": handler.process(command)}


@router.get("/api/v1/weather/{city_id}")
def weather_by_city(
    city_id: str, handler: CommandHandler = Depends(find_one_command_handler)
):
    command = FindOneWeatherCommand(city_id)
    weather = handler.process(command)
    return {
        "weather": {
            "temperature": weather.temperature,
            "city": weather.city,
        }
    }
