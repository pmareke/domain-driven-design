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
        weather_request: Weather = Weather(temperature=0, city="London")
        repository = PyMongoWeatherRepository()

        weather_id = repository.save(weather_request)
        weather = repository.find(weather_id)

        assert weather
        expect(weather_request.city).to(equal(weather.city))
        expect(weather_request.temperature).not_to(be(-10))

    def test_deletes_a_weathers(self) -> None:
        weather_request: Weather = Weather(temperature=0, city="London")
        repository = PyMongoWeatherRepository()

        weather_id = repository.save(weather_request)

        weather = repository.find(weather_id)
        assert weather

        repository.delete(weather_id)
        weather = repository.find(weather_id)
        assert not weather

    def test_updates_a_weathers(self) -> None:
        weather: Weather = Weather(temperature=0, city="London")
        repository = PyMongoWeatherRepository()

        weather_id = repository.save(weather)

        new_weather = repository.update(
            weather_id, Weather(temperature=10, city="Paris")
        )
        assert new_weather

        expect(weather.city).not_to(equal(new_weather.city))
        expect(weather.temperature).not_to(equal(new_weather.temperature))
