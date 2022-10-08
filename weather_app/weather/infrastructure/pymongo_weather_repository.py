from typing import List, Dict, Optional
import pymongo
from pymongo import MongoClient
from pymongo.results import InsertOneResult
from bson.objectid import ObjectId
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.weather import Weather, WeatherDTO


class PyMongoWeatherRepository(WeatherRepository):
    def __init__(self) -> None:
        client: MongoClient = pymongo.MongoClient(
            "mongodb://mongo:27017/weather"
        )
        self.database = client.weather

    def find_all(self) -> List[Weather]:
        weathers = self.database.weather.find()
        return [self._create_weather(weather) for weather in weathers]

    def find(self, city_id: str) -> Optional[Weather]:
        weather = self.database.weather.find_one({"_id": ObjectId(city_id)})
        if not weather:
            return None
        return self._create_weather(weather)

    def save(self, weather_dto: WeatherDTO) -> str:
        record: InsertOneResult = self.database.weather.insert_one(
            {
                "temperature": weather_dto.temperature,
                "city": weather_dto.city
            }
        )
        return str(record.inserted_id)

    @staticmethod
    def _create_weather(weather: Dict) -> Weather:
        return Weather(
            weather_id=str(ObjectId(weather["_id"])),
            temperature=weather["temperature"],
            city=weather["city"]
        )
