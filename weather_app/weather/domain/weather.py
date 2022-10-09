from dataclasses import dataclass


@dataclass
class Weather:
    weather_id: str
    temperature: int
    city: str

    def __init__(self, weather_id: str, temperature: int, city: str) -> None:
        self.temperature = temperature
        self.city = city
        self.weather_id = weather_id
        self._validate()

    def _validate(self) -> None:
        if self.city == "":
            raise WeatherInvalidException()
        if self.temperature > 100 or self.temperature < -100:
            raise WeatherInvalidException()


class WeatherNotFoundException(Exception):
    pass


class WeatherInvalidException(Exception):
    pass
