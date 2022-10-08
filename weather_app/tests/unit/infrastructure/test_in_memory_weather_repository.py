from expects import expect, be_empty
from weather_app.weather.infrastructure.in_memory_weather_repository import InMemoryWeatherRepository


class TestInMemoryWeatherRepository:
    def test_finds_all_weathers(self) -> None:
        repository = InMemoryWeatherRepository()

        weathers = repository.find_all()

        expect(weathers).not_to(be_empty)
