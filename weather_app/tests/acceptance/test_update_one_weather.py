from bson.objectid import ObjectId
from expects import expect, be, equal
from fastapi.testclient import TestClient
from fastapi import status

from weather_app.main import app

client = TestClient(app)


class TestWeather:
    def test_updates_a_weather(self) -> None:
        weather_id = str(ObjectId())
        city = "London"
        temperature = 10
        client.post(
            "/api/v1/weather",
            json={
                "weather_id": weather_id,
                "temperature": temperature,
                "city": city
            }
        )
        update_response = client.put(
            f"/api/v1/weather/{weather_id}",
            json={
                "temperature": 100,
                "city": "Roma"
            }
        )

        expect(update_response.status_code).to(be(status.HTTP_204_NO_CONTENT))

        get_response = client.get(f"/api/v1/weather/{weather_id}")
        get_json = get_response.json()
        expect(get_json["city"]).not_to(equal(city))
        expect(get_json["temperature"]).not_to(equal(temperature))

    def test_returns_not_found(self) -> None:
        any_weather_id = "507f1f77bcf86cd799439011"
        response = client.put(
            f"/api/v1/weather/{any_weather_id}",
            json={
                "temperature": 100,
                "city": "Madrid"
            }
        )

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_404_NOT_FOUND))
        expect(weather_json["detail"]).to(
            equal(f"Weather {any_weather_id} not found")
        )

    def test_returns_bad_request(self) -> None:
        any_weather_id = "507f1f77bcf86cd799439011"
        invalid_city = ""
        payload = {"temperature": 100, "city": invalid_city}
        response = client.put(f"/api/v1/weather/{any_weather_id}", json=payload)

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_400_BAD_REQUEST))
        expect(weather_json["detail"]).to(
            equal(
                f"The request temperature: {payload['temperature']}, city: {payload['city']} is not valid"
            )
        )

    def test_returns_bad_request_when_the_id_is_not_valid(self) -> None:
        any_weather_id = "any-invalid-id"
        payload = {"temperature": 100, "city": "London"}
        response = client.put(f"/api/v1/weather/{any_weather_id}", json=payload)

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_400_BAD_REQUEST))
        expect(weather_json["detail"]).to(
            equal(
                f"The request temperature: {payload['temperature']}, city: {payload['city']} is not valid"
            )
        )
