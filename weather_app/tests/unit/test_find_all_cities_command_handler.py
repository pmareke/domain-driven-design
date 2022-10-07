from expects import expect, be, be_empty
from doublex import Stub
from weather.domain.weather_repository import WeatherRepository
from weather.domain.weather import Weather
from weather.use_cases.find_all_weathers_command import FindAllWeathersCommand, FindAllWeathersCommandHandler


class TestFindAllWeathersCommandHandler:
    def test_finds_all_the_weathers(self):
        command = FindAllWeathersCommand()
        weather = Weather(id="any-id", temperature=20, city="Madrid")
        with Stub(WeatherRepository) as repository:
            repository.find_all().returns([weather])
        handler = FindAllWeathersCommandHandler(repository)

        response = handler.process(command)
        print(response)

        expect(response[0].city).to(be(weather.city))
