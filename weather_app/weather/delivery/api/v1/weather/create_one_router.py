from fastapi import APIRouter, Depends, Response, HTTPException
from fastapi import status
from weather_app.weather.delivery.api.v1.weather.weather_request import WeatherRequest
from weather_app.weather.domain.command_handler import CommandHandler
from weather_app.weather.domain.weather import WeatherInvalidException
from weather_app.weather.use_cases.create_one_weather_command import CreateOneWeatherCommand, CreateOneWeatherCommandHandler
from weather_app.weather.infrastructure.pymongo_weather_repository import PyMongoWeatherRepository

create_one_router = APIRouter()


async def _create_one_command_handler() -> CommandHandler:
    repository = PyMongoWeatherRepository()
    return CreateOneWeatherCommandHandler(repository)


@create_one_router.post("/api/v1/weather", response_model=None)
def create_weather(
    weather_request: WeatherRequest,
    response: Response,
    handler: CommandHandler = Depends(_create_one_command_handler)
) -> None:
    try:
        command = CreateOneWeatherCommand(
            weather_request.weather_id, weather_request.temperature,
            weather_request.city
        )
        handler.process(command)
        response.status_code = status.HTTP_201_CREATED
    except WeatherInvalidException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=
            f"The request temperature: {weather_request.temperature}, city: {weather_request.city} is not valid"
        ) from exception
