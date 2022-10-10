from expects import expect
from doublex import Spy
from doublex_expects import have_been_called_with

from weather_app.tests.helper.test_data import TestData, WeatherBuilder
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.use_cases.create_one_weather_command import CreateOneWeatherCommand, CreateOneWeatherCommandHandler


class TestCreateOneWeatherCommandHandler:
    def test_create_one_weather(self) -> None:
        weather = WeatherBuilder().build()
        command = CreateOneWeatherCommand(
            weather_id=TestData.ANY_WEATHER_ID, temperature=TestData.ANY_TEMPERATURE, city=TestData.ANY_CITY
        )
        repository = Spy(WeatherRepository)
        handler = CreateOneWeatherCommandHandler(repository)

        handler.process(command)

        expect(repository.save).to(have_been_called_with(weather))
