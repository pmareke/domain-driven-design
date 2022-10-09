from expects import expect
from doublex import Spy
from doublex_expects import have_been_called_with
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.use_cases.create_one_weather_command import CreateOneWeatherCommand, CreateOneWeatherCommandHandler
from weather_app.weather.domain.weather import Weather


class TestCreateOneWeatherCommandHandler:
    def test_create_one_weather(self) -> None:
        weather_id = "any-weather-id"
        temperature = 20
        city = "Madrid"
        weather = Weather(weather_id, temperature, city)
        command = CreateOneWeatherCommand(
            weather_id=weather_id, temperature=temperature, city=city
        )
        repository = Spy(WeatherRepository)
        handler = CreateOneWeatherCommandHandler(repository)

        handler.process(command)

        expect(repository.save).to(have_been_called_with(weather))
