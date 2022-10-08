from expects import expect, raise_error
from doublex import Stub, ANY_ARG
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.use_cases.delete_one_weather_command import DeleteOneWeatherCommand, DeleteOneWeatherCommandHandler


class TestDeleteOneWeatherCommandHandler:
    def test_delete_one_weather(self) -> None:
        weather_id = "any-weather_id"
        command = DeleteOneWeatherCommand(weather_id)
        with Stub(WeatherRepository) as repository:
            repository.delete(ANY_ARG)
        handler = DeleteOneWeatherCommandHandler(repository)

        expect(lambda: handler.process(command)).not_to(raise_error)
