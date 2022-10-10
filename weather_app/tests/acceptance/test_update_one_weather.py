from expects import expect, be, equal
from fastapi.testclient import TestClient
from fastapi import status

from weather_app.tests.helper.test_data import TestData
from weather_app.main import app

client = TestClient(app)


class TestWeather:

    def test_updates_a_weather(self) -> None:
        client.post("/api/v1/weather",
                    json={
                        "weather_id": TestData.ANY_WEATHER_ID,
                        "temperature": TestData.ANY_TEMPERATURE,
                        "city": TestData.ANY_CITY
                    })
        update_response = client.put(
            f"/api/v1/weather/{TestData.ANY_WEATHER_ID}",
            json={
                "temperature": 100,
                "city": "Roma"
            })

        expect(update_response.status_code).to(be(status.HTTP_204_NO_CONTENT))

        get_response = client.get(f"/api/v1/weather/{TestData.ANY_WEATHER_ID}")
        get_json = get_response.json()
        expect(get_json["city"]).not_to(equal(TestData.ANY_CITY))
        expect(get_json["temperature"]).not_to(equal(TestData.ANY_TEMPERATURE))

    def test_returns_not_found(self) -> None:
        any_weather_id = "507f1f77bcf86cd799439011"
        response = client.put(f"/api/v1/weather/{any_weather_id}",
                              json={
                                  "temperature": TestData.ANY_TEMPERATURE,
                                  "city": TestData.ANY_CITY
                              })

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_404_NOT_FOUND))
        expect(weather_json["detail"]).to(
            equal(f"Weather {any_weather_id} not found"))

    def test_returns_bad_request(self) -> None:
        invalid_city = ""
        payload = {
            "temperature": TestData.ANY_TEMPERATURE,
            "city": invalid_city
        }
        response = client.put(f"/api/v1/weather/{TestData.ANY_WEATHER_ID}",
                              json=payload)

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_400_BAD_REQUEST))
        expect(weather_json["detail"]).to(
            equal(
                f"The request id: {TestData.ANY_WEATHER_ID}, temperature: {TestData.ANY_TEMPERATURE}, city: {invalid_city} is not valid"
            ))

    def test_returns_bad_request_when_the_id_is_not_valid(self) -> None:
        any_weather_id = "any-invalid-id"
        payload = {
            "temperature": TestData.ANY_TEMPERATURE,
            "city": TestData.ANY_CITY
        }
        response = client.put(f"/api/v1/weather/{any_weather_id}", json=payload)

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_400_BAD_REQUEST))
        expect(weather_json["detail"]).to(
            equal(
                f"The request id: {any_weather_id}, temperature: {TestData.ANY_TEMPERATURE}, city: {TestData.ANY_CITY} is not valid"
            ))
