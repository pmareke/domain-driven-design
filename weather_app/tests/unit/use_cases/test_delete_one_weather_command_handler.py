from expects import expect
from doublex import Spy
from doublex_expects import have_been_called_with

from weather_app.tests.helper.test_data import TestData
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.use_cases.delete_one_weather_command import (
    DeleteOneWeatherCommand,
    DeleteOneWeatherCommandHandler,
)


class TestDeleteOneWeatherCommandHandler:

    def test_delete_one_weather(self) -> None:
        command = DeleteOneWeatherCommand(TestData.ANY_WEATHER_ID)
        repository = Spy(WeatherRepository)
        handler = DeleteOneWeatherCommandHandler(repository)

        handler.process(command)

        expect(repository.delete).to(have_been_called_with(TestData.ANY_WEATHER_ID))
