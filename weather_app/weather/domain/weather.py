from dataclasses import dataclass


@dataclass
class Weather:
    weather_id: str
    temperature: int
    city: str


class WeatherNotFoundException(Exception):
    pass
