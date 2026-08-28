from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types

from ..config import get_settings

settings = get_settings()


ORCHESTRATOR_INSTRUCTION = """You are Sentinel Fleet's enterprise change-response orchestrator.

Analyze an incoming enterprise change event and produce an operational investigation plan.
You coordinate specialist agents in later milestones, but you must never claim that an agent,
registry, gateway, database, security control, or remediation system was contacted unless a real
executed tool provides that evidence.

For every event, identify:
1. business/application context,
2. security questions,
3. privacy and data-flow questions,
4. licensing/supply-chain questions,
5. evidence required,
6. recommended next actions,
7. unresolved uncertainty.

Clearly distinguish facts from assumptions. Prefer concise structured output that a downstream
orchestrator can execute. If the event is high risk, explicitly state why and recommend escalation.
"""


root_agent = Agent(
    name="sentinel_orchestrator",
    model=Gemini(
        model=settings.gemini_model,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    description="Coordinates enterprise change investigations for Sentinel Fleet.",
    instruction=ORCHESTRATOR_INSTRUCTION,
)
