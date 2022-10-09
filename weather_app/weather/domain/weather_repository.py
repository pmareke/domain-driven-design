from abc import ABC, abstractmethod
from typing import List, Optional
from weather_app.weather.domain.weather import Weather


class WeatherRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Weather]:
        pass

    @abstractmethod
    def find(self, weather_id: str) -> Optional[Weather]:
        pass

    @abstractmethod
    def save(self, weather: Weather) -> str:
        pass

    @abstractmethod
    def delete(self, weather_id: str) -> None:
        pass

    @abstractmethod
    def update(self, weather_id: str, weather: Weather) -> Weather:
        pass
