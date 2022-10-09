from dataclasses import dataclass


@dataclass
class Weather:
    temperature: int
    city: str
    weather_id: str

    def __init__(
        self, temperature: int, city: str, weather_id: str = ""
    ) -> None:
        self.temperature = temperature
        self.city = city
        self.weather_id = weather_id
        self._validate()

    @classmethod
    def from_database(
        cls, temperature: int, city: str, weather_id: str
    ) -> "Weather":
        return cls(temperature=temperature, city=city, weather_id=weather_id)

    def _validate(self) -> None:
        if self.city == "":
            raise WeatherInvalidException()
        if self.temperature > 100 or self.temperature < -100:
            raise WeatherInvalidException()


class WeatherNotFoundException(Exception):
    pass


class WeatherInvalidException(Exception):
    pass
