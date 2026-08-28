from fastapi import FastAPI

from .config import get_settings
from .models import ChangeEvent, HealthResponse

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Autonomous enterprise AI security and change response platform.",
)


@app.get("/health", response_model=HealthResponse, tags=["system"])
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        version=settings.app_version,
        environment=settings.environment,
    )


@app.get("/", tags=["system"])
def root() -> dict[str, str]:
    return {
        "service": settings.app_name,
        "version": settings.app_version,
        "status": "ready",
    }


@app.post("/api/v1/events/validate", tags=["events"])
def validate_event(event: ChangeEvent) -> dict[str, object]:
    """Validate the canonical event contract before orchestration is added."""
    return {
        "accepted": True,
        "event_id": event.event_id,
        "event_type": event.event_type,
        "message": "Event contract validated.",
    }
