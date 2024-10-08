from expects import expect, be_none, equal

from weather_app.tests.helper.test_data import TestData, WeatherBuilder
from weather_app.weather.domain.weather import Weather
from weather_app.weather.infrastructure.in_memory_weather_repository import (
    InMemoryWeatherRepository,
)


class TestInMemoryWeatherRepository:

    def test_finds_all_weathers(self) -> None:
        repository = InMemoryWeatherRepository()
        weather = WeatherBuilder().with_weather_id(TestData.ANY_WEATHER_ID).build()

        repository.save(weather)
        records = repository.find_all()

        expect(records[0].weather_id).to(equal(TestData.ANY_WEATHER_ID))

    def test_finds_one_weather(self) -> None:
        repository = InMemoryWeatherRepository()
        weather = WeatherBuilder().with_weather_id(TestData.ANY_WEATHER_ID).build()

        repository.save(weather)
        record = repository.find(TestData.ANY_WEATHER_ID)
        assert record

        expect(record.weather_id).to(equal(TestData.ANY_WEATHER_ID))

    def test_saves_one_weather(self) -> None:
        repository = InMemoryWeatherRepository()
        weather = WeatherBuilder().with_weather_id(TestData.ANY_WEATHER_ID).build()

        repository.save(weather)
        record = repository.find(TestData.ANY_WEATHER_ID)
        assert record

        expect(record.weather_id).to(equal(TestData.ANY_WEATHER_ID))

    def test_deletes_one_weather(self) -> None:
        repository = InMemoryWeatherRepository()
        weather = WeatherBuilder().with_weather_id(TestData.ANY_WEATHER_ID).build()

        repository.save(weather)
        record = repository.find(TestData.ANY_WEATHER_ID)
        assert record

        expect(record.weather_id).to(equal(TestData.ANY_WEATHER_ID))

        repository.delete(TestData.ANY_WEATHER_ID)

        record = repository.find(TestData.ANY_WEATHER_ID)
        expect(record).to(be_none)

    def test_updates_one_weather(self) -> None:
        repository = InMemoryWeatherRepository()
        weather = WeatherBuilder().with_weather_id(TestData.ANY_WEATHER_ID).build()

        repository.save(weather)
        new_temperature = 100
        new_city = "London"
        updated_weather: Weather = (
            WeatherBuilder()
            .with_temperature(new_temperature)
            .with_city(new_city)
            .build()
        )
        record = repository.update(updated_weather)
        assert record

        expect(record.temperature).to(equal(new_temperature))
        expect(record.city).to(equal(new_city))
