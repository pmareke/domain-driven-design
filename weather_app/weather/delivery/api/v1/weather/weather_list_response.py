from typing import List
from dataclasses import dataclass
from weather_app.weather.delivery.api.v1.weather.weather_response import WeatherResponse


@dataclass
class WeatherListResponse:
    weathers: List[WeatherResponse]
