from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_update_rates():
    response = client.post("/update-rates")
    assert response.status_code == 200
    assert response.json() == {"message": "Rates updated."}


def test_last_update():
    response = client.get("/last-update")
    assert response.status_code == 200
    assert response.json().get("last_update") is not None
    assert isinstance(response.json().get("last_update"), str)


def test_conversion_fail():
    params = dict(target="USD", amount=1, source="AUD")

    response = client.get("/conversion", params=params)
    assert response.status_code == 404
