from fastapi import APIRouter, Depends, Response, status, HTTPException
from weather_app.weather.delivery.api.v1.weather.weather_request import WeatherRequest
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather import Weather, WeatherNotFoundException, WeatherInvalidException
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
    weather_request: WeatherRequest,
    response: Response,
    handler: CommandHandler = Depends(_update_one_command_handler)
) -> Weather:
    try:
        weather = Weather(weather_id=weather_id, temperature=weather_request.temperature, city=weather_request.city)
        command = UpdateOneWeatherCommand(weather)
        updated_weather = handler.process(command)
    except WeatherInvalidException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The request temperature: {weather_request.temperature}, city: {weather_request.city} is not valid"
        )from exception
    except WeatherNotFoundException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Weather {weather_id} not found"
        ) from exception

    response.status_code = status.HTTP_204_NO_CONTENT
    weather: Weather = updated_weather.weather
    return weather
