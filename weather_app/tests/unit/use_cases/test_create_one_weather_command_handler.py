from expects import expect, be
from doublex import Stub, ANY_ARG
from weather_app.weather.domain.weather import Weather
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.use_cases.create_one_weather_command import CreateOneWeatherCommand, CreateOneWeatherCommandHandler, CreateOneWeatherCommandResponse


class TestCreateOneWeatherCommandHandler:
    def test_create_one_weather(self) -> None:
        weather_id = "any-weather_id"
        weather = Weather(weather_id=weather_id, temperature=20, city="Madrid")
        command = CreateOneWeatherCommand(weather)
        with Stub(WeatherRepository) as repository:
            repository.save(ANY_ARG).returns(weather_id)
        handler = CreateOneWeatherCommandHandler(repository)

        response: CreateOneWeatherCommandResponse = handler.process(command)

        expect(response.weather_id).to(be(weather_id))
