from expects import expect, be
from doublex import Stub, ANY_ARG
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.use_cases.create_one_weather_command import CreateOneWeatherCommand, CreateOneWeatherCommandHandler, CreateOneWeatherCommandResponse


class TestCreateOneWeatherCommandHandler:
    def test_create_one_weather(self) -> None:
        weather_id = "any-weather_id"
        command = CreateOneWeatherCommand(20, "Madrid")
        with Stub(WeatherRepository) as repository:
            repository.save(ANY_ARG).returns(weather_id)
        handler = CreateOneWeatherCommandHandler(repository)

        response: CreateOneWeatherCommandResponse = handler.process(command)

        expect(response.weather_id).to(be(weather_id))
