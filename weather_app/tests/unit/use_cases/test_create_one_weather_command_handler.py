from expects import expect
from doublex import Spy
from doublex_expects import have_been_called_with

from weather_app.tests.helper.test_data import TestData
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.use_cases.create_one_weather_command import CreateOneWeatherCommand, CreateOneWeatherCommandHandler
from weather_app.weather.domain.weather import Weather


class TestCreateOneWeatherCommandHandler:
    def test_create_one_weather(self) -> None:
        weather = Weather(TestData.ANY_WEATHER_ID, TestData.ANY_TEMPERATURE, TestData.ANY_CITY)
        command = CreateOneWeatherCommand(
            weather_id=TestData.ANY_WEATHER_ID, temperature=TestData.ANY_TEMPERATURE, city=TestData.ANY_CITY
        )
        repository = Spy(WeatherRepository)
        handler = CreateOneWeatherCommandHandler(repository)

        handler.process(command)

        expect(repository.save).to(have_been_called_with(weather))
