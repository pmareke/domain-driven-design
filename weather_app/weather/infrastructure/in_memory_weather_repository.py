import json
import uuid
from typing import List
from weather.domain.weather_repository import WeatherRepository
from weather.domain.weather import Weather


class InMemoryWeatherRepository(WeatherRepository):
    def find_all(self) -> List[Weather]:
        with open("data/weathers.json", "r") as file:
            weathers = json.load(file)
        return [
            Weather(
                id=weather["id"],
                temperature=weather["temperature"],
                city=weather["city"]
            ) for weather in weathers
        ]

    def find(self, city_id: str) -> Weather:
        return Weather(id=uuid.uuid1(), temperature=30, city="Madrid")
