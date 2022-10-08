from expects import expect, be, equal
from fastapi.testclient import TestClient
from fastapi import status

from weather_app.main import app


client = TestClient(app)


class TestWeather:
    def test_updates_a_weather(self) -> None:
        city = "London"
        temperature = 10
        response = client.post(
            "/api/v1/weather", json={
                "temperature": temperature,
                "city": city
            }
        )
        weather_id = response.json()["id"]
        update_response = client.put(
            f"/api/v1/weather/{weather_id}", json={
                "temperature": 100,
                "city": "Roma"
            }
        )

        expect(update_response.status_code).to(be(status.HTTP_204_NO_CONTENT))

        get_response = client.get(f"/api/v1/weather/{weather_id}")
        get_json = get_response.json()
        expect(get_json["city"]).not_to(equal(city))
        expect(get_json["temperature"]).not_to(equal(temperature))
