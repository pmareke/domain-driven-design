import pymongo
from bson.objectid import ObjectId
from typing import List
from weather.domain.weather_repository import WeatherRepository
from weather.domain.weather import Weather


class PyMongoWeatherRepository(WeatherRepository):
    def __init__(self) -> None:
        client = pymongo.MongoClient("mongodb://mongo:27017/weather")
        self.db = client.weather

    def find_all(self) -> List[Weather]:
        weathers = self.db.weather.find()
        return [
            Weather(
                id=str(ObjectId(weather["_id"])),
                temperature=weather["temperature"],
                city=weather["city"]
            ) for weather in weathers
        ]

    def find(self, city_id: str) -> Weather:
        weather = self.db.weather.find_one({"_id": ObjectId(city_id)})
        return Weather(
            id=str(ObjectId(weather["_id"])),
            temperature=weather["temperature"],
            city=weather["city"]
        )
