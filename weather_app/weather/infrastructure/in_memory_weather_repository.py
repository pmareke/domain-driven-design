from typing import List, Optional
import uuid
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.weather import Weather


class InMemoryWeatherRepository(WeatherRepository):
    def __init__(self) -> None:
        self.weathers: List[Weather] = []

    def find_all(self) -> List[Weather]:
        return self.weathers

    def find(self, weather_id: str) -> Optional[Weather]:
        for weather in self.weathers:
            if weather.weather_id == weather_id:
                return weather
        return None

    def save(self, weather: Weather) -> str:
        weather = Weather(
            weather_id=str(uuid.uuid1()),
            temperature=weather.temperature,
            city=weather.city
        )
        self.weathers.append(weather)
        return weather.weather_id

    def delete(self, weather_id: str) -> None:
        for weather in self.weathers:
            if weather.weather_id == weather_id:
                self.weathers.remove(weather)
                break

    def update(self, weather: Weather) -> Optional[Weather]:
        for weather in self.weathers:
            if weather.weather_id == weather.weather_id:
                weather.city = weather.city
                weather.temperature = weather.temperature
                return weather
        return None
