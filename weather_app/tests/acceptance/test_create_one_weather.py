from bson.objectid import ObjectId
from expects import expect, be, equal
from fastapi.testclient import TestClient
from fastapi import status

from weather_app.main import app

client = TestClient(app)


class TestWeather:
    def test_creates_a_weather(self) -> None:
        weather_id = str(ObjectId())
        response = client.post(
            "/api/v1/weather",
            json={
                "weather_id": weather_id,
                "temperature": 100,
                "city": "Roma"
            }
        )

        expect(response.status_code).to(be(status.HTTP_201_CREATED))

        response = client.get(f"/api/v1/weather/{weather_id}")
        expect(response.status_code).to(be(status.HTTP_200_OK))

    def test_returns_bad_request(self) -> None:
        invalid_city = ""
        weather_id = str(ObjectId())
        payload = {
            "weather_id": weather_id,
            "temperature": 100,
            "city": invalid_city
        }
        response = client.post("/api/v1/weather", json=payload)

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_400_BAD_REQUEST))
        expect(weather_json["detail"]).to(
            equal(
                f"The request temperature: {payload['temperature']}, city: {payload['city']} is not valid"
            )
        )

    def test_returns_bad_request_when_the_id_is_not_correct(self) -> None:
        payload = {
            "weather_id": "any-invalid-id",
            "temperature": 100,
            "city": "Madrid"
        }
        response = client.post("/api/v1/weather", json=payload)

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_400_BAD_REQUEST))
        expect(weather_json["detail"]).to(
            equal(
                f"The request temperature: {payload['temperature']}, city: {payload['city']} is not valid"
            )
        )
