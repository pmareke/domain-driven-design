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

        city_id = created_weather["id"]
        response = client.get(f"/api/v1/weather/{city_id}")

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_200_OK))
        expect(weather_json["city"]).to(equal("Roma"))
        expect(weather_json["temperature"]).to(equal(100))
