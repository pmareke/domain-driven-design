from expects import expect, be
from doublex import Stub, ANY_ARG

from weather_app.tests.helper.test_data import TestData, WeatherBuilder
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.use_cases.update_one_weather_command import UpdateOneWeatherCommandHandler, \
    UpdateOneWeatherCommandResponse, UpdateOneWeatherCommand


class TestUpdateOneWeatherCommandHandler:
    def test_update_one_weather(self) -> None:
        weather = WeatherBuilder().build()
        command = UpdateOneWeatherCommand(weather_id=TestData.ANY_WEATHER_ID, temperature=TestData.ANY_TEMPERATURE, city=TestData.ANY_CITY)
        with Stub(WeatherRepository) as repository:
            repository.update(ANY_ARG).returns(weather)
        handler = UpdateOneWeatherCommandHandler(repository)

        response: UpdateOneWeatherCommandResponse = handler.process(command)

        expect(response.weather.city).to(be(TestData.ANY_CITY))
