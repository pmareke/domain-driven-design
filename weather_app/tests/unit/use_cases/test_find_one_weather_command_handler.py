from expects import expect, be, be_empty
from doublex import Stub, ANY_ARG
from weather.domain.weather_repository import WeatherRepository
from weather.domain.weather import Weather
from weather.use_cases.find_one_weather_command import FindOneWeatherCommand, FindOneWeatherCommandHandler


class TestFindOneWeatherCommandHandler:
    def test_finds_one_weather(self):
        city_id = "any-id"
        weather = Weather(id=city_id, temperature=20, city="Madrid")
        command = FindOneWeatherCommand(city_id)
        with Stub(WeatherRepository) as repository:
            repository.find(ANY_ARG).returns(weather)
        handler = FindOneWeatherCommandHandler(repository)

        response = handler.process(command)

        expect(response.city).to(be(weather.city))
