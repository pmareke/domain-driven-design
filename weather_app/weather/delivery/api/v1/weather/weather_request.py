from dataclasses import dataclass

@dataclass
class WeatherRequest:
    temperature: int
    city: str
