from expects import expect, be, be_true
from fastapi.testclient import TestClient
from fastapi import status

from main import app

client = TestClient(app)


class TestWeather:
    def test_health(self):
        response = client.get("/health")

        expect(response.status_code).to(be(status.HTTP_200_OK))
        expect(response.json()["ok"]).to(be_true)
