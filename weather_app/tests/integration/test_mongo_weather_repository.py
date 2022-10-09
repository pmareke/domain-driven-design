from bson.objectid import ObjectId
from expects import expect, be, be_empty, equal
from weather_app.weather.domain.weather import Weather
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

        expect(weather.city).to(equal(city_weather.city))
        expect(weather.temperature).not_to(be(-10))

    def test_creates_a_weathers(self) -> None:
        weather_id = str(ObjectId())
        weather: Weather = Weather(
            weather_id=weather_id, temperature=0, city="London"
        )
        repository = PyMongoWeatherRepository()

        repository.save(weather)
        record = repository.find(weather_id)
        assert record

        expect(record.weather_id).to(equal(weather_id))

    def test_deletes_a_weathers(self) -> None:
        weather_id = str(ObjectId())
        weather: Weather = Weather(
            weather_id=weather_id, temperature=0, city="London"
        )
        repository = PyMongoWeatherRepository()

        repository.save(weather)

        record = repository.find(weather_id)
        assert record

        repository.delete(weather_id)
        record = repository.find(weather_id)
        assert not record

    def test_updates_a_weather(self) -> None:
        weather_id = str(ObjectId())
        weather: Weather = Weather(
            weather_id=weather_id, temperature=0, city="London"
        )
        repository = PyMongoWeatherRepository()

        repository.save(weather)

        new_temperature = 10
        new_city = "Paris"
        record = repository.update(
            Weather(
                weather_id=weather_id,
                temperature=new_temperature,
                city=new_city
            )
        )
        assert record

        expect(record.city).to(equal(new_city))
        expect(record.temperature).to(equal(new_temperature))
