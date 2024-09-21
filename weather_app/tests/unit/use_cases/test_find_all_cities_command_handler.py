from expects import expect
from doublex import Spy
from doublex_expects import have_been_called

from weather_app.weather.domain.weather_repository import WeatherRepository
from weather_app.weather.use_cases.find_all_weathers_command import (
    FindAllWeathersCommand,
    FindAllWeathersCommandHandler,
)


class TestFindAllWeathersCommandHandler:

    def test_finds_all_the_weathers(self) -> None:
        command = FindAllWeathersCommand()
        repository = Spy(WeatherRepository)
        handler = FindAllWeathersCommandHandler(repository)

        handler.process(command)

        expect(repository.find_all).to(have_been_called)
