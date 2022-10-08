from expects import expect, be_empty, be_none, equal
from weather_app.weather.domain.weather import Weather
from weather_app.weather.infrastructure.in_memory_weather_repository import InMemoryWeatherRepository


class TestInMemoryWeatherRepository:
    def test_finds_all_weathers(self) -> None:
        repository = InMemoryWeatherRepository()
        weather = Weather(temperature=10, city="Paris")

        repository.save(weather)
        weathers = repository.find_all()

        expect(weathers).not_to(be_empty)

    def test_finds_one_weather(self) -> None:
        repository = InMemoryWeatherRepository()
        weather = Weather(temperature=10, city="Paris")

        weather_id = repository.save(weather)
        record = repository.find(weather_id)

        expect(record).not_to(be_none)

    def test_saves_one_weather(self) -> None:
        repository = InMemoryWeatherRepository()
        weather = Weather(temperature=10, city="Paris")

        weather_id = repository.save(weather)

        record = repository.find(weather_id)
        assert record

        expect(record.city).to(equal(weather.city))
        expect(record.temperature).to(equal(weather.temperature))

    def test_deletes_one_weather(self) -> None:
        repository = InMemoryWeatherRepository()
        weather = Weather(temperature=10, city="Paris")

        weather_id = repository.save(weather)

        record = repository.find(weather_id)
        assert record

        expect(record.city).to(equal(weather.city))
        expect(record.temperature).to(equal(weather.temperature))

        repository.delete(weather_id)

        record = repository.find(weather_id)
        expect(record).to(be_none)

    def test_updates_one_weather(self) -> None:
        weather: Weather = Weather(temperature=0, city="London")
        repository = InMemoryWeatherRepository()

        weather_id = repository.save(weather)
        new_weather: Weather = Weather(
            weather_id=weather_id, temperature=10, city="Paris"
        )

        record = repository.update(new_weather)
        assert record

        expect(record.city).not_to(equal(weather.city))
        expect(record.temperature).not_to(equal(weather.temperature))
