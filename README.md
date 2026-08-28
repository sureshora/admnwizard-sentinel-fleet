# AdmnWizard Sentinel Fleet

**Autonomous Enterprise AI Security & Change Response Platform**

> Hackathon track: **The Fortified Enterprise Fleet**

## SENTINEL-002 — Real ADK + Gemini Orchestrator

This milestone introduces the first real Google ADK agent and Gemini model configuration. The project now contains an ADK `Agent` and an ADK `App` that can be run through Google's current Agents CLI / ADK development tooling.

Google's current ADK project structure uses an `Agent`, an `App`, and a model configuration; the current official examples use `google-adk[gcp]` and Gemini Flash models. The project is therefore structured around that pattern rather than a simulated agent. 

## Architecture at this milestone

```text
Enterprise Change Event
        |
        v
  Sentinel API contract
        |
        v
  ADK / Gemini Orchestrator
        |
        v
Investigation Plan
        |
        +-----------------------------+
        | security questions          |
        | privacy/data-flow questions |
        | licensing questions         |
        | evidence required           |
        | next actions                 |
        | uncertainty                  |
        +-----------------------------+
```

Specialist agents, event transport, persistent memory, gateway, Model Armor, and production observability are intentionally reserved for later milestones. They must not be described as active until they are actually wired and verified.

## Prerequisites

- Python 3.11+
- Google Cloud project with Vertex AI access, or a Gemini API configuration supported by ADK
- Google authentication configured for the selected Gemini access path
- Optional: `uv` / Google's current Agents CLI for the ADK playground

## Local setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
Copy-Item .env.example .env
```

Set at minimum:

```text
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GEMINI_MODEL=gemini-3.7-flash
```

For Google Cloud authentication, use Application Default Credentials in the development environment. Do not commit credentials or `.env` files.

## Run the Sentinel API foundation

```powershell
uvicorn app.main:app --reload --port 8080
```

Health check:

```powershell
Invoke-RestMethod http://127.0.0.1:8080/health
```

## Run the real ADK agent

Install the current Google Agents CLI if desired:

```powershell
uvx google-agents-cli setup
```

Then from the repository root, use the ADK playground workflow supported by the current Agents CLI:

```powershell
agents-cli playground
```

Or run a single prompt:

```powershell
agents-cli run "Analyze this change: a customer-support AI application is adding an unapproved external AI API that will receive customer conversations. Produce the security, privacy, licensing, evidence, and next-action investigation plan."
```

The agent must be able to authenticate to Gemini for an actual model response. Without credentials/model access, local import and structural tests can still validate the application, but an LLM response cannot be honestly claimed.

## Test

```powershell
pytest
```

## Milestones

- [x] SENTINEL-001 — Repository & Runtime Foundation
- [x] SENTINEL-002 — ADK + Gemini Orchestrator
- [ ] SENTINEL-003 — Security / Privacy / License Agents
- [ ] SENTINEL-004 — Event-Driven Execution + Persistent State
- [ ] SENTINEL-005 — Agent Governance / Security Layer
- [ ] SENTINEL-006 — Observability + Execution Traces
- [ ] SENTINEL-007 — Sentinel Control Tower UI
- [ ] SENTINEL-008 — End-to-End Hackathon Demo Scenario
- [ ] SENTINEL-009 — README + Architecture + Deployment Proof
- [ ] SENTINEL-010 — Final Submission Package

## Engineering rule

Every milestone is a complete, reproducible checkpoint. Existing working files are preserved unless explicitly revised. Real Google capabilities are never represented as implemented until they are actually connected and verified.
