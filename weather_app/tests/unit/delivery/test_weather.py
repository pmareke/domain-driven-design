from expects import expect, equal, raise_error
from weather_app.weather.domain.weather import Weather, WeatherInvalidException


class TestWeather:
    def test_creates_a_weather(self) -> None:
        city = "Oviedo"
        weather = Weather(temperature=5, city=city)

        expect(weather.city).to(equal(city))

    def test_raise_an_error_is_the_city_is_not_valid(self) -> None:
        expect(lambda: Weather(temperature=10, city="")).to(
            raise_error(WeatherInvalidException)
        )

    def test_raise_an_error_is_the_temperature_is_not_valid(self) -> None:
        expect(lambda: Weather(temperature=10000, city="Madrid")).to(
            raise_error(WeatherInvalidException)
        )
