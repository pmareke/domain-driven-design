from expects import expect, be, raise_error
from doublex import Stub, ANY_ARG
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.weather import Weather, WeatherNotFoundException
from weather_app.weather.use_cases.find_one_weather_command import FindOneWeatherCommand, FindOneWeatherCommandHandler, \
    FindOneWeatherCommandResponse


class TestFindOneWeatherCommandHandler:
    def test_finds_one_weather(self) -> None:
        city_id = "any-weather_id"
        weather = Weather(weather_id=city_id, temperature=20, city="Madrid")
        command = FindOneWeatherCommand(city_id)
        with Stub(WeatherRepository) as repository:
            repository.find(ANY_ARG).returns(weather)
        handler = FindOneWeatherCommandHandler(repository)

        response: FindOneWeatherCommandResponse = handler.process(command)

        expect(response.weather.city).to(be(weather.city))

    def test_raises_an_error_when_the_weather_does_not_exist(self) -> None:
        city_id = "any-weather_id"
        command = FindOneWeatherCommand(city_id)
        with Stub(WeatherRepository) as repository:
            repository.find(ANY_ARG).returns(None)
        handler = FindOneWeatherCommandHandler(repository)

        expect(lambda: handler.process(command)).to(raise_error(WeatherNotFoundException))
