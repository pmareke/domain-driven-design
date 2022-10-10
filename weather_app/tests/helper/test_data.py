from bson.objectid import ObjectId

from weather_app.weather.domain.weather import Weather


class TestData:
    ANY_WEATHER_ID = str(ObjectId())
    ANY_TEMPERATURE = 10
    ANY_CITY = "any-city"

    @staticmethod
    def create_weather() -> Weather:
        return Weather(
            weather_id=TestData.ANY_WEATHER_ID,
            temperature=TestData.ANY_TEMPERATURE,
            city=TestData.ANY_CITY
        )
