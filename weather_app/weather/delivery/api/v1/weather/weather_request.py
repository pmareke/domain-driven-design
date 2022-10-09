from dataclasses import dataclass


@dataclass
class WeatherRequest:
    weather_id: str
    temperature: int
    city: str
