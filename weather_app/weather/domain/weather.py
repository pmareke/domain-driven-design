from dataclasses import dataclass
from lib2to3.pgen2.token import OP
from typing import Optional

@dataclass
class Weather:
    temperature: int
    city: str
    weather_id: Optional[str]

    def __init__(self, temperature: int, city: str, weather_id: Optional[str] = None) -> None:
        self.temperature = temperature
        self.city = city
        self.weather_id = weather_id
        if self.city == "":
            raise WeatherInvalidException()
        if self.temperature > 100 or self.temperature < -100:
            raise WeatherInvalidException()

class WeatherNotFoundException(Exception):
    pass


class WeatherInvalidException(Exception):
    pass
