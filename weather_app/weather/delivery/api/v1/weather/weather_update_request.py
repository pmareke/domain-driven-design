from dataclasses import dataclass


@dataclass
class WeatherUpdateRequest:
    temperature: int
    city: str
