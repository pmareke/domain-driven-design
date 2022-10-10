from expects import expect, be
from doublex import Stub

from weather_app.tests.helper.test_data import TestData, WeatherBuilder
from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.use_cases.find_all_weathers_command import FindAllWeathersCommand, \
    FindAllWeathersCommandHandler, FindAllWeathersCommandResponse


class TestFindAllWeathersCommandHandler:
    def test_finds_all_the_weathers(self) -> None:
        command = FindAllWeathersCommand()
        weather = WeatherBuilder().build()
        with Stub(WeatherRepository) as repository:
            repository.find_all().returns([weather])
        handler = FindAllWeathersCommandHandler(repository)

        response: FindAllWeathersCommandResponse = handler.process(command)

        expect(response.weathers[0].weather_id).to(be(TestData.ANY_WEATHER_ID))
