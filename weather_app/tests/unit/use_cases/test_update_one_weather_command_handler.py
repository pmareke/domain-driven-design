from expects import expect, be, raise_error
from doublex import Stub, ANY_ARG
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.weather import WeatherDTO, Weather, WeatherNotFoundException
from weather_app.weather.use_cases.update_one_weather_command import UpdateOneWeatherCommandHandler, \
    UpdateOneWeatherCommandResponse, UpdateOneWeatherCommand


class TestUpdateOneWeatherCommandHandler:
    def test_update_one_weather(self) -> None:
        weather_id = "any-weather_id"
        weather_dto = WeatherDTO(temperature=20, city="Madrid")
        weather = Weather(
            weather_id=weather_id,
            temperature=weather_dto.temperature,
            city=weather_dto.city
        )
        command = UpdateOneWeatherCommand(weather_id, weather_dto)
        with Stub(WeatherRepository) as repository:
            repository.update(ANY_ARG).returns(weather)
        handler = UpdateOneWeatherCommandHandler(repository)

        response: UpdateOneWeatherCommandResponse = handler.process(command)

        expect(response.weather.weather_id).to(be(weather_id))

    def test_raises_an_error_when_the_weather_does_not_exist(self) -> None:
        weather_id = "any-weather_id"
        weather_dto = WeatherDTO(0, "any-city")
        command = UpdateOneWeatherCommand(weather_id, weather_dto)
        with Stub(WeatherRepository) as repository:
            repository.find(ANY_ARG).returns(None)
        handler = UpdateOneWeatherCommandHandler(repository)

        expect(lambda: handler.process(command)).to(
            raise_error(WeatherNotFoundException)
        )