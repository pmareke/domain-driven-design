from expects import expect, be, be_empty, be_none, be_true, equal
from fastapi.testclient import TestClient
from fastapi import status

from weather_app.main import app

client = TestClient(app)


class TestWeather:
    def test_health(self) -> None:
        response = client.get("/health")

        expect(response.status_code).to(be(status.HTTP_200_OK))
        expect(response.json()["ok"]).to(be_true)

    def test_lists_the_weather_in_all_cities(self) -> None:
        response = client.get("/api/v1/weather")

        weathers = response.json()["weathers"]
        expect(response.status_code).to(be(status.HTTP_200_OK))
        expect(weathers).not_to(be_empty)

    def test_gets_the_weather_for_a_given_city(self) -> None:
        response = client.get("/api/v1/weather")
        weathers = response.json()["weathers"]
        city_id = weathers[0]["weather_id"]

        response = client.get(f"/api/v1/weather/{city_id}")

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_200_OK))
        expect(weather_json["city"]).not_to(be_none)

    def test_returns_not_found(self) -> None:
        any_non_existing_city_id = "507f1f77bcf86cd799439011"
        response = client.get(f"/api/v1/weather/{any_non_existing_city_id}")

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_404_NOT_FOUND))
        expect(weather_json["detail"]).to(equal(f"Weather {any_non_existing_city_id} not found"))
