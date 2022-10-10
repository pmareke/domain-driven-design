from expects import expect, be
from fastapi.testclient import TestClient
from fastapi import status

from weather_app.tests.helper.test_data import TestData
from weather_app.main import app

client = TestClient(app)


class TestWeather:
    def test_deletes_a_weather(self) -> None:
        response = client.post(
            "/api/v1/weather",
            json={
                "weather_id": TestData.ANY_WEATHER_ID,
                "temperature": TestData.ANY_TEMPERATURE,
                "city": TestData.ANY_CITY
            }
        )

        expect(response.status_code).to(be(status.HTTP_201_CREATED))

        response = client.delete(f"/api/v1/weather/{TestData.ANY_WEATHER_ID}")
        expect(response.status_code).to(be(status.HTTP_204_NO_CONTENT))

        response = client.get(f"/api/v1/weather/{TestData.ANY_WEATHER_ID}")
        expect(response.status_code).to(be(status.HTTP_404_NOT_FOUND))
