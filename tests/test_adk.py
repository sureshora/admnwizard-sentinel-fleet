from google.adk.agents import Agent

from app.agent import app, root_agent


def test_adk_root_agent() -> None:
    assert isinstance(root_agent, Agent)
    assert root_agent.name == "sentinel_orchestrator"
    assert root_agent.model is not None


def test_adk_app() -> None:
    assert app.name == "app"
    assert app.root_agent.name == "sentinel_orchestrator"
