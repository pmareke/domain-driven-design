from expects import expect, be, be_empty, be_none, be_true
from fastapi.testclient import TestClient
from fastapi import status

from main import app

client = TestClient(app)


class TestWeather:
    def test_health(self):
        response = client.get("/health")

        expect(response.status_code).to(be(status.HTTP_200_OK))
        expect(response.json()["ok"]).to(be_true)

    def test_lists_the_weather_in_all_cities(self):
        response = client.get("/api/v1/weather")
        weathers = response.json()["weathers"]

        expect(response.status_code).to(be(status.HTTP_200_OK))
        expect(weathers).not_to(be_empty)

    def test_gets_the_weather_for_a_given_city(self):
        response = client.get("/api/v1/weather/1")
        weather = response.json()["weather"]

        expect(response.status_code).to(be(status.HTTP_200_OK))
        expect(weather["city"]).not_to(be_none)
