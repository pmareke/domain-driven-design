from bson.objectid import ObjectId
from expects import expect, be_none, equal
from weather_app.weather.domain.weather import Weather
from weather_app.weather.infrastructure.in_memory_weather_repository import InMemoryWeatherRepository


class TestInMemoryWeatherRepository:
    def test_finds_all_weathers(self) -> None:
        weather_id = str(ObjectId())
        temperature = 10
        city = "Paris"
        repository = InMemoryWeatherRepository()
        weather = Weather(
            weather_id=weather_id, temperature=temperature, city=city
        )

        repository.save(weather)
        records = repository.find_all()

        expect(records[0].weather_id).to(equal(weather_id))

    def test_finds_one_weather(self) -> None:
        weather_id = str(ObjectId())
        temperature = 10
        city = "Paris"
        repository = InMemoryWeatherRepository()
        weather = Weather(
            weather_id=weather_id, temperature=temperature, city=city
        )

        repository.save(weather)
        record = repository.find(weather_id)
        assert record

        expect(record.weather_id).to(equal(weather_id))

    def test_saves_one_weather(self) -> None:
        weather_id = str(ObjectId())
        temperature = 10
        city = "Paris"
        repository = InMemoryWeatherRepository()
        weather = Weather(
            weather_id=weather_id, temperature=temperature, city=city
        )

        repository.save(weather)
        record = repository.find(weather_id)
        assert record

        expect(record.weather_id).to(equal(weather_id))

    def test_deletes_one_weather(self) -> None:
        weather_id = str(ObjectId())
        temperature = 10
        city = "Paris"
        repository = InMemoryWeatherRepository()
        weather = Weather(
            weather_id=weather_id, temperature=temperature, city=city
        )

        repository.save(weather)
        record = repository.find(weather_id)
        assert record

        expect(record.weather_id).to(equal(weather_id))

        repository.delete(weather_id)

        record = repository.find(weather_id)
        expect(record).to(be_none)

    def test_updates_one_weather(self) -> None:
        weather_id = str(ObjectId())
        temperature = 10
        city = "Paris"
        repository = InMemoryWeatherRepository()
        weather = Weather(
            weather_id=weather_id, temperature=temperature, city=city
        )

        repository.save(weather)
        updated_weather: Weather = Weather(
            weather_id=weather_id, temperature=100, city="London"
        )
        record = repository.update(updated_weather)
        assert record

        expect(record.city).not_to(equal(weather.city))
        expect(record.temperature).not_to(equal(weather.temperature))
