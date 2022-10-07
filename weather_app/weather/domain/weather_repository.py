from abc import ABC, abstractmethod
from typing import List
from weather.domain.weather import Weather


class WeatherRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Weather]:
        pass

    @abstractmethod
    def find(self, city_id: str) -> Weather:
        pass
