from typing import List, Dict
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.weather import Weather


class PyMongoWeatherRepository(WeatherRepository):
    def __init__(self) -> None:
        client: MongoClient = pymongo.MongoClient("mongodb://mongo:27017/weather")
        self.database = client.weather

    def find_all(self) -> List[Weather]:
        weathers = self.database.weather.find()
        return [self._create_weather(weather) for weather in weathers]

    def find(self, city_id: str) -> Weather:
        weather = self.database.weather.find_one({"_id": ObjectId(city_id)})
        if not weather:
            # TODO - Add missing test
            raise Exception
        return self._create_weather(weather)

    @staticmethod
    def _create_weather(weather: Dict) -> Weather:
        return Weather(
            weather_id=str(ObjectId(weather["_id"])),
            temperature=weather["temperature"],
            city=weather["city"]
        )
