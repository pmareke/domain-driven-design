from dataclasses import dataclass
from bson.objectid import ObjectId
from bson.errors import InvalidId


@dataclass
class Weather:
    weather_id: str
    temperature: int
    city: str

    def __init__(self, weather_id: str, temperature: int, city: str) -> None:
        self.temperature = temperature
        self.city = city
        self.weather_id = weather_id


class WeatherFactory:
    @staticmethod
    def make(weather_id: str, temperature: int, city: str) -> Weather:
        try:
            ObjectId(weather_id)
        except InvalidId as exception:
            raise WeatherInvalidException() from exception

        if city == "":
            raise WeatherInvalidException()
        if temperature > 100 or temperature < -100:
            raise WeatherInvalidException()

        return Weather(weather_id, temperature, city)


class WeatherNotFoundException(Exception):
    pass


class WeatherInvalidException(Exception):
    pass
