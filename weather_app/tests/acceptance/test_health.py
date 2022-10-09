from expects import expect, be, be_true
from fastapi.testclient import TestClient
from fastapi import status

from weather_app.main import app

client = TestClient(app)


class TestHeath:
    def test_health(self) -> None:
        response = client.get("/api/v1/health")

        expect(response.status_code).to(be(status.HTTP_200_OK))
        expect(response.json()["ok"]).to(be_true)
