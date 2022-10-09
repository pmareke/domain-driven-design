from fastapi import APIRouter, Depends, status, HTTPException
from weather_app.weather.delivery.api.v1.weather.weather_update_request import WeatherUpdateRequest
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather import WeatherNotFoundException, WeatherInvalidException
from weather_app.weather.infrastructure.pymongo_weather_repository import PyMongoWeatherRepository
from weather_app.weather.use_cases.update_one_weather_command import UpdateOneWeatherCommand, \
    UpdateOneWeatherCommandHandler

update_one_router = APIRouter()


async def _update_one_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return UpdateOneWeatherCommandHandler(repository)


@update_one_router.put(
    "/api/v1/weather/{weather_id}", status_code=status.HTTP_204_NO_CONTENT
)
def update_weather(
    weather_id: str,
    weather_request: WeatherUpdateRequest,
    handler: CommandHandler = Depends(_update_one_command_handler)
) -> None:
    try:
        command = UpdateOneWeatherCommand(
            weather_id, weather_request.temperature, weather_request.city
        )
        handler.process(command)
    except WeatherInvalidException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=
            f"The request temperature: {weather_request.temperature}, city: {weather_request.city} is not valid"
        ) from exception
    except WeatherNotFoundException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Weather {weather_id} not found"
        ) from exception
