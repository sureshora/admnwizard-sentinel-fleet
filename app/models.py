from datetime import datetime, timezone
from enum import StrEnum

from pydantic import BaseModel, Field


class EventType(StrEnum):
    APPLICATION_CHANGE = "application_change"
    DATA_FLOW_CHANGE = "data_flow_change"
    DEPLOYMENT_CHANGE = "deployment_change"


class ChangeEvent(BaseModel):
    """Canonical event contract used by Sentinel Fleet."""

    event_id: str = Field(min_length=1)
    event_type: EventType
    application: str = Field(min_length=1)
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    source: str = Field(min_length=1)
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: dict[str, object] = Field(default_factory=dict)


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    environment: str
