from expects import expect, be, be_empty, equal
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

        weather = repository.find(city_id=city_weather.weather_id)

        expect(weather.city).to(equal(city_weather.city))
        expect(weather.temperature).not_to(be(-10))
