from typing import Dict, List, Optional
from collections import defaultdict
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.weather import Weather


class InMemoryWeatherRepository(WeatherRepository):

    def __init__(self) -> None:
        self.weathers: Dict[str, Weather] = defaultdict()

    def find_all(self) -> List[Weather]:
        return list(self.weathers.values())

    def find(self, weather_id: str) -> Optional[Weather]:
        return self.weathers.get(weather_id)

    def save(self, weather: Weather) -> None:
        self.weathers[weather.weather_id] = weather

    def delete(self, weather_id: str) -> None:
        del self.weathers[weather_id]

    def update(self, weather: Weather) -> Optional[Weather]:
        self.weathers[weather.weather_id] = weather
        return weather
