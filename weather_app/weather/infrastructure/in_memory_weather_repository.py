from typing import List
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.weather import Weather


class InMemoryWeatherRepository(WeatherRepository):
    def find_all(self) -> List[Weather]:
        return [self._create_weather()]

    def find(self, city_id: str) -> Weather:
        return self._create_weather()

    @staticmethod
    def _create_weather() -> Weather:
        return Weather(
            weather_id="6340b8b096886afc9b16d259", temperature=30, city="Madrid"
        )
