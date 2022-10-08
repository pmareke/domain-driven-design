from typing import List
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.weather import Weather, WeatherDTO


class InMemoryWeatherRepository(WeatherRepository):
    def __init__(self) -> None:
        self.weathers: List[Weather] = [self._create_weather()]

    def find_all(self) -> List[Weather]:
        return self.weathers

    def find(self, city_id: str) -> Weather:
        return self.weathers[0]

    def save(self, weather_dto: WeatherDTO) -> str:
        weather = Weather(
            weather_id="6340b8b096886afc9b16d259",
            temperature=weather_dto.temperature,
            city=weather_dto.city
        )
        self.weathers.append(weather)
        return weather.weather_id

    @staticmethod
    def _create_weather() -> Weather:
        return Weather(
            weather_id="6340b8b096886afc9b16d259",
            temperature=30,
            city="Madrid"
        )
