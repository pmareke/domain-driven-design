from bson.objectid import ObjectId
from expects import expect, be_empty, equal

from weather_app.tests.helper.test_data import WeatherBuilder
from weather_app.weather.infrastructure.pymongo_weather_repository import PyMongoWeatherRepository


class TestPyMongoWeatherRepository:
    def test_finds_all_the_weathers(self) -> None:
        repository = PyMongoWeatherRepository()

        weathers = repository.find_all()

        expect(weathers).not_to(be_empty)

    def test_finds_one_weather(self) -> None:
        repository = PyMongoWeatherRepository()
        weathers = repository.find_all()
        city_weather = weathers[0]
        assert city_weather.weather_id

        weather = repository.find(weather_id=city_weather.weather_id)
        assert weather

        expect(weather.weather_id).to(equal(city_weather.weather_id))

    def test_creates_a_weathers(self) -> None:
        weather_id = str(ObjectId())
        weather = WeatherBuilder().with_weather_id(weather_id).build()
        repository = PyMongoWeatherRepository()

        repository.save(weather)
        record = repository.find(weather_id)
        assert record

        expect(record.weather_id).to(equal(weather_id))

    def test_deletes_a_weathers(self) -> None:
        weather_id = str(ObjectId())
        weather = WeatherBuilder().with_weather_id(weather_id).build()
        repository = PyMongoWeatherRepository()

        repository.save(weather)

        record = repository.find(weather_id)
        assert record

        repository.delete(weather_id)
        record = repository.find(weather_id)
        assert not record

    def test_updates_a_weather(self) -> None:
        weather_id = str(ObjectId())
        weather = WeatherBuilder().with_weather_id(weather_id).build()
        repository = PyMongoWeatherRepository()

        repository.save(weather)

        new_temperature = 10
        new_city = "Paris"
        record = repository.update(
            WeatherBuilder().with_weather_id(weather_id).
            with_temperature(new_temperature).with_city(new_city).build()
        )
        assert record

        expect(record.city).to(equal(new_city))
        expect(record.temperature).to(equal(new_temperature))
