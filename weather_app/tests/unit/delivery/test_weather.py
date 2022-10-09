from bson.objectid import ObjectId
from expects import expect, equal, raise_error
from weather_app.weather.domain.weather import Weather, WeatherInvalidException


class TestWeather:
    def test_creates_a_weather(self) -> None:
        weather_id = str(ObjectId())
        city = "Oviedo"
        weather = Weather(weather_id=weather_id, temperature=5, city=city)

        expect(weather.city).to(equal(city))

    def test_raise_an_error_is_the_city_is_not_valid(self) -> None:
        weather_id = str(ObjectId())
        expect(lambda: Weather(weather_id=weather_id, temperature=10, city="")
              ).to(raise_error(WeatherInvalidException))

    def test_raise_an_error_is_the_temperature_is_not_valid(self) -> None:
        weather_id = str(ObjectId())
        expect(
            lambda:
            Weather(weather_id=weather_id, temperature=10000, city="Madrid")
        ).to(raise_error(WeatherInvalidException))

    def test_raise_an_error_is_the_id_is_not_valid(self) -> None:
        weather_id = "any-invalid-id"
        expect(
            lambda:
            Weather(weather_id=weather_id, temperature=10, city="Madrid")
        ).to(raise_error(WeatherInvalidException))
