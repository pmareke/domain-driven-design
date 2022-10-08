from expects import expect, be, be_empty, equal
from weather_app.weather.infrastructure.pymongo_weather_repository import PyMongoWeatherRepository
from weather_app.weather.domain.weather import WeatherDTO


class TestPyMongoWeatherRepository:
    def test_finds_all_the_weathers(self) -> None:
        repository = PyMongoWeatherRepository()

        weathers = repository.find_all()

        expect(weathers).not_to(be_empty)

    def test_finds_one_weather(self) -> None:
        repository = PyMongoWeatherRepository()
        weathers = repository.find_all()
        city_weather = weathers[0]

        weather = repository.find(weather_id=city_weather.weather_id)
        assert weather

        expect(weather.city).to(equal(city_weather.city))
        expect(weather.temperature).not_to(be(-10))

    def test_creates_a_weathers(self) -> None:
        weather_dto: WeatherDTO = WeatherDTO(temperature=0, city="London")
        repository = PyMongoWeatherRepository()

        weather_id = repository.save(weather_dto)
        weather = repository.find(weather_id)

        assert weather
        expect(weather_dto.city).to(equal(weather.city))
        expect(weather_dto.temperature).not_to(be(-10))

    def test_deletes_a_weathers(self) -> None:
        weather_dto: WeatherDTO = WeatherDTO(temperature=0, city="London")
        repository = PyMongoWeatherRepository()

        weather_id = repository.save(weather_dto)

        weather = repository.find(weather_id)
        assert weather

        repository.delete(weather_id)
        weather = repository.find(weather_id)
        assert not weather

    def test_updates_a_weathers(self) -> None:
        weather_dto: WeatherDTO = WeatherDTO(temperature=0, city="London")
        new_weather_dto: WeatherDTO = WeatherDTO(temperature=10, city="Paris")
        repository = PyMongoWeatherRepository()

        weather_id = repository.save(weather_dto)

        weather = repository.update(weather_id, new_weather_dto)
        assert weather

        expect(weather_dto.city).not_to(equal(weather.city))
        expect(weather_dto.temperature).not_to(equal(weather.temperature))
