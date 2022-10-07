import uuid
from typing import List
from weather.domain.weather_repository import WeatherRepository
from weather.domain.weather import Weather


class InMemoryWeatherRepository(WeatherRepository):
    def find_all(self) -> List[Weather]:
        return [Weather(id=uuid.uuid1(), temperature=30, city="Madrid")]

    def find(self, city_id: str) -> Weather:
        return Weather(id=uuid.uuid1(), temperature=30, city="Madrid")
