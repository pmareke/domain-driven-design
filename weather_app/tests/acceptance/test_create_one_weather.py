from expects import expect, be, equal
from fastapi.testclient import TestClient
from fastapi import status

from weather_app.main import app

client = TestClient(app)


class TestWeather:
    def test_creates_a_weather(self) -> None:
        response = client.post(
            "/api/v1/weather", json={
                "temperature": 100,
                "city": "Roma"
            }
        )

        created_weather = response.json()

        expect(response.status_code).to(be(status.HTTP_201_CREATED))

        weather_id = created_weather["weather_id"]
        response = client.get(f"/api/v1/weather/{weather_id}")

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_200_OK))
        expect(weather_json["city"]).to(equal("Roma"))
        expect(weather_json["temperature"]).to(equal(100))

    def test_returns_not_bad_request(self) -> None:
        invalid_city = ""
        payload = {"temperature": 100, "city": invalid_city}
        response = client.post("/api/v1/weather", json=payload)

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_400_BAD_REQUEST))
        expect(weather_json["detail"]).to(
            equal(
                f"The request temperature: {payload['temperature']}, city: {payload['city']} is not valid"
            )
        )
