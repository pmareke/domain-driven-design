from dataclasses import dataclass


@dataclass
class WeatherDTO:
    temperature: int
    city: str

    def validate(self) -> None:
        if self.city == "":
            raise WeatherDTOInvalidException()
        if self.temperature > 100 or self.temperature < -100:
            raise WeatherDTOInvalidException()

    def __str__(self) -> str:
        return f"temperature: {self.temperature}, city: {self.city}"


@dataclass
class Weather(WeatherDTO):
    weather_id: str


class WeatherNotFoundException(Exception):
    pass


class WeatherDTOInvalidException(Exception):
    pass
