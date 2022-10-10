from expects import expect, be, be_empty
from fastapi.testclient import TestClient
from fastapi import status

from weather_app.main import app

client = TestClient(app)


class TestWeather:

    def test_lists_the_weathers(self) -> None:
        response = client.get("/api/v1/weather")

        weathers = response.json()["weathers"]
        expect(response.status_code).to(be(status.HTTP_200_OK))
        expect(weathers).not_to(be_empty)
