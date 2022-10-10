from expects import expect, raise_error
from doublex import Stub, Mock, ANY_ARG
from doublex_expects import have_been_satisfied

from weather_app.tests.helper.test_data import TestData, WeatherBuilder
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.weather import WeatherNotFoundException
from weather_app.weather.use_cases.find_one_weather_command import FindOneWeatherCommand, FindOneWeatherCommandHandler


class TestFindOneWeatherCommandHandler:
    def test_finds_one_weather(self) -> None:
        command = FindOneWeatherCommand(TestData.ANY_WEATHER_ID)
        with Mock(WeatherRepository) as repository:
            repository.find(TestData.ANY_WEATHER_ID).returns(WeatherBuilder().build())
        handler = FindOneWeatherCommandHandler(repository)

        handler.process(command)

        expect(repository).to(have_been_satisfied)

    def test_raises_an_error_when_the_weather_does_not_exist(self) -> None:
        command = FindOneWeatherCommand(TestData.ANY_WEATHER_ID)
        with Stub(WeatherRepository) as repository:
            repository.find(ANY_ARG).returns(None)
        handler = FindOneWeatherCommandHandler(repository)

        expect(lambda: handler.process(command)).to(
            raise_error(WeatherNotFoundException)
        )
