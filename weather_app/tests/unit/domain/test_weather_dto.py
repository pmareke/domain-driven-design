from expects import expect, equal, raise_error
from weather_app.weather.domain.weather import WeatherDTO, WeatherDTOInvalidException


class TestWeatherDTO:
    def test_creates_a_weather_dto(self) -> None:
        city = "Oviedo"
        weather_dto = WeatherDTO(temperature=5, city=city)

        expect(weather_dto.city).to(equal(city))

    def test_raise_an_error_is_the_city_is_not_valid(self) -> None:
        weather_dto = WeatherDTO(temperature=10, city="")

        expect(lambda: weather_dto.validate()).to(
            raise_error(WeatherDTOInvalidException)
        )

    def test_raise_an_error_is_the_temperature_is_not_valid(self) -> None:
        weather_dto = WeatherDTO(temperature=10000, city="Madrid")

        expect(lambda: weather_dto.validate()).to(
            raise_error(WeatherDTOInvalidException)
        )
