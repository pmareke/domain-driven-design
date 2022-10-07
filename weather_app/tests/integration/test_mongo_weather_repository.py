from expects import expect, be, be_empty, equal
from weather.infrastructure.pymongo_weather_repository import PyMongoWeatherRepository


class TestPyMongoWeatherRepository:
    def test_finds_all_the_weathers(self):
        repository = PyMongoWeatherRepository()

        weathers = repository.find_all()

        expect(weathers).not_to(be_empty)

    def test_finds_onee_weather(self):
        repository = PyMongoWeatherRepository()
        weathers = repository.find_all()
        city_weather = weathers[0]

        weather = repository.find(city_id=city_weather.id)

        expect(weather.city).to(equal(city_weather.city))
        expect(weather.temperature).not_to(be(-10))
