from expects import expect, be
from doublex import Stub
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.domain.weather import Weather
from weather_app.weather.use_cases.find_all_weathers_command import FindAllWeathersCommand, \
    FindAllWeathersCommandHandler, FindAllWeathersCommandResponse


class TestFindAllWeathersCommandHandler:
    def test_finds_all_the_weathers(self) -> None:
        command = FindAllWeathersCommand()
        weather = Weather(weather_id="any-weather_id", temperature=20, city="Madrid")
        with Stub(WeatherRepository) as repository:
            repository.find_all().returns([weather])
        handler = FindAllWeathersCommandHandler(repository)

        response: FindAllWeathersCommandResponse = handler.process(command)

        expect(response.weathers[0].city).to(be(weather.city))
