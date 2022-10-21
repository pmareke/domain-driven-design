from typing import List, Dict, Optional
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.weather import Weather


class PyMongoWeatherRepository(WeatherRepository):
    def __init__(self) -> None:
        client: MongoClient = pymongo.MongoClient(
            "mongodb://mongo:27017/weather"
        )
        self.database = client.weather

    def find_all(self) -> List[Weather]:
        weathers = self.database.weather.find()
        return [self._create_weather(weather) for weather in weathers]

    def find(self, weather_id: str) -> Optional[Weather]:
        weather = self.database.weather.find_one({"_id": ObjectId(weather_id)})
        return None if not weather else self._create_weather(weather)

    def save(self, weather: Weather) -> None:
        self.database.weather.insert_one(
            {
                "_id": ObjectId(weather.weather_id),
                "temperature": weather.temperature,
                "city": weather.city
            }
        )

    def delete(self, weather_id: str) -> None:
        self.database.weather.delete_one({"_id": ObjectId(weather_id)})

    def update(self, weather: Weather) -> Optional[Weather]:
        record = self.database.weather.update_one(
            {"_id": ObjectId(weather.weather_id)}, {
                '$set':
                    {
                        'city': weather.city,
                        'temperature': weather.temperature,
                    }
            },
            upsert=False
        )
        return None if not record else self.find(weather.weather_id)

    @staticmethod
    def _create_weather(weather: Dict) -> Weather:
        return Weather(
            weather_id=str(ObjectId(weather["_id"])),
            temperature=weather["temperature"],
            city=weather["city"]
        )
