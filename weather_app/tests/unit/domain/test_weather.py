from expects import expect, equal, raise_error

from weather_app.tests.helper.test_data import TestData, WeatherBuilder
from weather_app.weather.domain.weather import WeatherInvalidException


class TestWeather:

    def test_creates_a_weather(self) -> None:
        weather = WeatherBuilder().with_weather_id(
            TestData.ANY_WEATHER_ID).build()

        expect(weather.city).to(equal(TestData.ANY_CITY))

    def test_raise_an_error_is_the_city_is_not_valid(self) -> None:
        invalid_city = ""
        expect(lambda: WeatherBuilder().with_city(invalid_city).build()).to(
            raise_error(WeatherInvalidException))

    def test_raise_an_error_is_the_temperature_is_not_valid(self) -> None:
        invalid_temperature = 10000
        expect(lambda: WeatherBuilder().with_temperature(invalid_temperature).
               build()).to(raise_error(WeatherInvalidException))

    def test_raise_an_error_is_the_id_is_not_valid(self) -> None:
        invalid_id = "invalid-id"
        expect(lambda: WeatherBuilder().with_weather_id(invalid_id).build()).to(
            raise_error(WeatherInvalidException))
