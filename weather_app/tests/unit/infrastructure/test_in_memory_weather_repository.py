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
        weather = repository.find(weather_id)

        expect(weather).not_to(be_none)

    def test_saves_one_weather(self) -> None:
        repository = InMemoryWeatherRepository()
        weather_ = Weather(temperature=10, city="Paris")

        weather_id = repository.save(weather_)

        weather = repository.find(weather_id)
        assert weather

        expect(weather.city).to(equal(weather.city))
        expect(weather.temperature).to(equal(weather.temperature))

    def test_deletes_one_weather(self) -> None:
        repository = InMemoryWeatherRepository()
        weather = Weather(temperature=10, city="Paris")

        weather_id = repository.save(weather)

        weather = repository.find(weather_id)
        assert weather

        expect(weather.city).to(equal(weather.city))
        expect(weather.temperature).to(equal(weather.temperature))

        repository.delete(weather_id)

        weather = repository.find(weather_id)
        expect(weather).to(be_none)

    def test_updates_one_weather(self) -> None:
        weather: Weather = Weather(temperature=0, city="London")
        repository = InMemoryWeatherRepository()

        weather_id = repository.save(weather)
        new_weather: Weather = Weather(weather_id=weather_id, temperature=10, city="Paris")

        weather = repository.update(new_weather)
        assert weather

        expect(weather.city).not_to(equal(new_weather.city))
        expect(weather.temperature).not_to(equal(new_weather.temperature))
