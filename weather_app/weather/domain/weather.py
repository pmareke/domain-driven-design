from dataclasses import dataclass


@dataclass
class WeatherDTO:
    temperature: int
    city: str


@dataclass
class Weather(WeatherDTO):
    weather_id: str


class WeatherNotFoundException(Exception):
    pass
