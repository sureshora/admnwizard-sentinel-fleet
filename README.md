# AdmnWizard Sentinel Fleet

**Autonomous Enterprise AI Security & Change Response Platform**

> Hackathon track: **The Fortified Enterprise Fleet**

Sentinel Fleet is an event-driven enterprise agent system designed to discover approved agents, investigate risky application changes, retain investigation context, enforce security policies, and produce auditable remediation decisions.

## Current milestone

**SENTINEL-001 — Repository & Runtime Foundation**

This milestone establishes the reproducible Python service foundation, configuration model, event contract, health endpoint, and development commands. Google Cloud/ADK integrations are introduced in subsequent milestones and will only be described as active after they are actually wired and verified.

## Planned architecture

```text
Enterprise Change Event
        |
        v
     Pub/Sub
        |
        v
 ADK Orchestrator
        |
   +----+----+----------------+
   |         |                |
   v         v                v
Security   Privacy         License
 Agent      Agent            Agent
   |         |                |
   +---------+----------------+
             |
             v
       Risk Synthesizer
             |
       +-----+-----+
       |           |
       v           v
   Remediation   Audit
       |           |
       +-----+-----+
             v
     Observability
```

## Repository structure

```text
admnwizard-sentinel-fleet/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   └── models.py
├── tests/
│   ├── __init__.py
│   └── test_foundation.py
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

## Local setup

Python 3.11+ is recommended.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

Create environment configuration:

```powershell
Copy-Item .env.example .env
```

Run the service:

```powershell
uvicorn app.main:app --reload --port 8080
```

Verify:

```powershell
Invoke-RestMethod http://127.0.0.1:8080/health
```

Run tests:

```powershell
pytest
```

## Engineering rules

- Complete files are committed; milestone changes are not distributed as partial diffs.
- Existing working files are preserved unless a milestone explicitly revises them.
- No simulated Google Cloud capability will be presented as a real integration.
- Every major integration must have a demonstrable verification path.
- Hackathon implementation is optimized for the official Fortified Enterprise Fleet requirements and the judging criteria: operational utility, architectural discipline, and demo/production readiness.

## Milestones

- [x] SENTINEL-001 — Repository & Runtime Foundation
- [ ] SENTINEL-002 — ADK + Gemini Orchestrator
- [ ] SENTINEL-003 — Security / Privacy / License Agents
- [ ] SENTINEL-004 — Event-Driven Execution + Persistent State
- [ ] SENTINEL-005 — Agent Governance / Security Layer
- [ ] SENTINEL-006 — Observability + Execution Traces
- [ ] SENTINEL-007 — Sentinel Control Tower UI
- [ ] SENTINEL-008 — End-to-End Hackathon Demo Scenario
- [ ] SENTINEL-009 — README + Architecture + Deployment Proof
- [ ] SENTINEL-010 — Final Submission Package
