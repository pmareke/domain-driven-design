from expects import expect, raise_error
from doublex import Mock, Stub, ANY_ARG
from doublex_expects import have_been_satisfied

from weather_app.tests.helper.test_data import TestData, WeatherBuilder
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.weather import WeatherNotFoundException
from weather_app.weather.use_cases.update_one_weather_command import (
    UpdateOneWeatherCommandHandler,
    UpdateOneWeatherCommand,
)


class TestUpdateOneWeatherCommandHandler:

    def test_update_one_weather(self) -> None:
        weather = WeatherBuilder().build()
        command = UpdateOneWeatherCommand(
            weather_id=TestData.ANY_WEATHER_ID,
            temperature=TestData.ANY_TEMPERATURE,
            city=TestData.ANY_CITY,
        )
        with Mock(WeatherRepository) as repository:
            repository.update(weather).returns(weather)
        handler = UpdateOneWeatherCommandHandler(repository)

        handler.process(command)

        expect(repository).to(have_been_satisfied)

    def test_raises_an_error_when_the_weather_does_not_exist(self) -> None:
        command = UpdateOneWeatherCommand(
            TestData.ANY_WEATHER_ID, TestData.ANY_TEMPERATURE, TestData.ANY_CITY
        )
        with Stub(WeatherRepository) as repository:
            repository.find(ANY_ARG).returns(None)
        handler = UpdateOneWeatherCommandHandler(repository)

        expect(lambda: handler.process(command)).to(
            raise_error(WeatherNotFoundException)
        )
