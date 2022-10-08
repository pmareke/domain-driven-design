from fastapi import APIRouter, Depends, Response
from fastapi import status
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather import WeatherDTO, Weather
from weather_app.weather.infrastructure.pymongo_weather_repository import PyMongoWeatherRepository
from weather_app.weather.use_cases.update_one_weather_command import UpdateOneWeatherCommand, \
    UpdateOneWeatherCommandHandler

update_one_router = APIRouter()


async def _update_one_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return UpdateOneWeatherCommandHandler(repository)


@update_one_router.put("/api/v1/weather/{weather_id}", response_model=Weather)
def update_weather(
    weather_id: str,
    weather_dto: WeatherDTO,
    response: Response,
    handler: CommandHandler = Depends(_update_one_command_handler)
) -> Weather:
    command = UpdateOneWeatherCommand(weather_id, weather_dto)
    updated_weather = handler.process(command)
    response.status_code = status.HTTP_204_NO_CONTENT
    weather: Weather = updated_weather.weather
    return weather
