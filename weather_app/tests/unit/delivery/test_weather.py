from bson.objectid import ObjectId
from expects import expect, equal, raise_error

from weather_app.tests.helper.test_data import TestData
from weather_app.weather.domain.weather import Weather, WeatherInvalidException


class TestWeather:
    def test_creates_a_weather(self) -> None:
        weather = Weather(weather_id=str(ObjectId()), temperature=TestData.ANY_TEMPERATURE, city=TestData.ANY_CITY)

        expect(weather.city).to(equal(TestData.ANY_CITY))

    def test_raise_an_error_is_the_city_is_not_valid(self) -> None:
        invalid_city = ""

        expect(lambda: Weather(weather_id=str(ObjectId()), temperature=TestData.ANY_TEMPERATURE, city=invalid_city)
              ).to(raise_error(WeatherInvalidException))

    def test_raise_an_error_is_the_temperature_is_not_valid(self) -> None:
        invalid_temperature = 10000

        expect(
            lambda:
            Weather(weather_id=str(ObjectId()), temperature=invalid_temperature, city=TestData.ANY_CITY)
        ).to(raise_error(WeatherInvalidException))

    def test_raise_an_error_is_the_id_is_not_valid(self) -> None:
        invalid_weather_id = "any-invalid-weather-id"

        expect(
            lambda:
            Weather(weather_id=invalid_weather_id, temperature=TestData.ANY_TEMPERATURE, city=TestData.ANY_CITY)
        ).to(raise_error(WeatherInvalidException))
