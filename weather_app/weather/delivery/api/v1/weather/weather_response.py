from dataclasses import dataclass


@dataclass
class WeatherResponse:
    weather_id: str
    temperature: int
    city: str
