from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["service"] == "AdmnWizard Sentinel Fleet"


def test_validate_change_event() -> None:
    payload = {
        "event_id": "evt-demo-001",
        "event_type": "application_change",
        "application": "Customer Support AI",
        "title": "New external AI API integration",
        "description": "A deployment adds an external AI provider.",
        "source": "demo",
        "metadata": {"external_endpoint": "example.invalid"},
    }
    response = client.post("/api/v1/events/validate", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["accepted"] is True
    assert body["event_id"] == "evt-demo-001"
