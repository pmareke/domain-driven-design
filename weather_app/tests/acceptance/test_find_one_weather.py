from expects import expect, be, be_none, equal
from fastapi.testclient import TestClient
from fastapi import status

from weather_app.main import app

client = TestClient(app)


class TestWeather:
    def test_gets_the_weather_for_a_given_city(self) -> None:
        response = client.get("/api/v1/weather")
        weathers = response.json()["weathers"]
        weather_id = weathers[0]["weather_id"]

        response = client.get(f"/api/v1/weather/{weather_id}")

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_200_OK))
        expect(weather_json["city"]).not_to(be_none)

    def test_returns_not_found(self) -> None:
        any_non_existing_weather_id = "507f1f77bcf86cd799439011"
        response = client.get(f"/api/v1/weather/{any_non_existing_weather_id}")

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_404_NOT_FOUND))
        expect(weather_json["detail"]).to(
            equal(f"Weather {any_non_existing_weather_id} not found")
        )
