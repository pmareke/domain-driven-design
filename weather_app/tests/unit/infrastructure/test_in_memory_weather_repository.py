from expects import expect, be_empty, be_none, equal
from weather_app.weather.infrastructure.in_memory_weather_repository import InMemoryWeatherRepository
from weather_app.weather.domain.weather import WeatherDTO


class TestInMemoryWeatherRepository:
    def test_finds_all_weathers(self) -> None:
        repository = InMemoryWeatherRepository()
        weather_dto = WeatherDTO(temperature=10, city="Paris")

        repository.save(weather_dto)
        weathers = repository.find_all()

        expect(weathers).not_to(be_empty)

    def test_finds_one_weather(self) -> None:
        repository = InMemoryWeatherRepository()
        weather_dto = WeatherDTO(temperature=10, city="Paris")

        weather_id = repository.save(weather_dto)
        weather = repository.find(weather_id)

        expect(weather).not_to(be_none)

    def test_saves_one_weather(self) -> None:
        repository = InMemoryWeatherRepository()
        weather_dto = WeatherDTO(temperature=10, city="Paris")

        weather_id = repository.save(weather_dto)

        weather = repository.find(weather_id)
        assert weather

        expect(weather.city).to(equal(weather_dto.city))
        expect(weather.temperature).to(equal(weather_dto.temperature))

    def test_deletes_one_weather(self) -> None:
        repository = InMemoryWeatherRepository()
        weather_dto = WeatherDTO(temperature=10, city="Paris")

        weather_id = repository.save(weather_dto)

        weather = repository.find(weather_id)
        assert weather

        expect(weather.city).to(equal(weather_dto.city))
        expect(weather.temperature).to(equal(weather_dto.temperature))

        repository.delete(weather_id)

        weather = repository.find(weather_id)
        expect(weather).to(be_none)
