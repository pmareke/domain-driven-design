from bson.objectid import ObjectId

from weather_app.weather.domain.weather import Weather, WeatherFactory


class TestData:
    ANY_WEATHER_ID = str(ObjectId())
    ANY_TEMPERATURE = 10
    ANY_CITY = "any-city"


class WeatherBuilder:

    def __init__(self) -> None:
        self._weather_id = TestData.ANY_WEATHER_ID
        self._temperature = TestData.ANY_TEMPERATURE
        self._city = TestData.ANY_CITY

    def with_weather_id(self, weather_id: str) -> "WeatherBuilder":
        self._weather_id = weather_id
        return self

    def with_temperature(self, temperature: int) -> "WeatherBuilder":
        self._temperature = temperature
        return self

    def with_city(self, city: str) -> "WeatherBuilder":
        self._city = city
        return self

    def build(self) -> Weather:
        return WeatherFactory.make(
            weather_id=self._weather_id, temperature=self._temperature, city=self._city
        )
