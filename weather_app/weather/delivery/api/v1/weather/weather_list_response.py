from typing import List
from dataclasses import dataclass

from weather_app.weather.domain.weather import Weather


@dataclass
class WeatherListResponse:
    weathers: List[Weather]
