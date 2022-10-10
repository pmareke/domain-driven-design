from expects import expect, be, equal
from fastapi.testclient import TestClient
from fastapi import status

from weather_app.tests.helper.test_data import TestData
from weather_app.main import app

client = TestClient(app)


class TestWeather:

    def test_creates_a_weather(self) -> None:
        response = client.post("/api/v1/weather",
                               json={
                                   "weather_id": TestData.ANY_WEATHER_ID,
                                   "temperature": TestData.ANY_TEMPERATURE,
                                   "city": TestData.ANY_CITY
                               })

        expect(response.status_code).to(be(status.HTTP_201_CREATED))

        response = client.get(f"/api/v1/weather/{TestData.ANY_WEATHER_ID}")
        expect(response.status_code).to(be(status.HTTP_200_OK))

    def test_returns_bad_request(self) -> None:
        invalid_city = ""
        payload = {
            "weather_id": TestData.ANY_WEATHER_ID,
            "temperature": TestData.ANY_TEMPERATURE,
            "city": invalid_city
        }
        response = client.post("/api/v1/weather", json=payload)

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_400_BAD_REQUEST))
        expect(weather_json["detail"]).to(
            equal(
                f"The request id: {TestData.ANY_WEATHER_ID}, temperature: {TestData.ANY_TEMPERATURE}, city: {invalid_city} is not valid"
            ))

    def test_returns_bad_request_when_the_id_is_not_correct(self) -> None:
        any_invalid_id = "any-invalid-id"
        payload = {
            "weather_id": any_invalid_id,
            "temperature": TestData.ANY_TEMPERATURE,
            "city": TestData.ANY_CITY
        }
        response = client.post("/api/v1/weather", json=payload)

        weather_json = response.json()
        expect(response.status_code).to(be(status.HTTP_400_BAD_REQUEST))
        expect(weather_json["detail"]).to(
            equal(
                f"The request id: {any_invalid_id}, temperature: {TestData.ANY_TEMPERATURE}, city: {TestData.ANY_CITY} is not valid"
            ))
