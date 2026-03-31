# Edge AI Ops Platform

Edge AI Ops Platform is a frontend-first full-stack starter for IoT operations, AI event monitoring, and industrial inspection workflows.

The goal is to provide a serious product foundation for operator-facing dashboards instead of a generic admin panel demo.

## Product Focus

- fleet visibility for edge and IoT devices
- live telemetry and heartbeat monitoring
- AI event operations for detections, anomalies, and alerts
- inspection workflows with evidence and traceability
- dense operational dashboards with drill-down views

## Stack

- Frontend: React, TypeScript, Vite, Tailwind CSS, TanStack Query, React Router
- Backend: FastAPI, SQLAlchemy, Pydantic, Uvicorn
- Data: PostgreSQL
- Realtime: WebSocket-ready backend and frontend architecture
- Docs: MkDocs Material
- Local development: Docker Compose and Makefile

## Planned Modules

- auth
- devices
- telemetry
- ai-events
- inspections
- alerts
- dashboards
- settings

## Repo Layout

```text
edge-ai-ops-platform/
  backend/
  frontend/
  docs/
  docker-compose.yml
  Makefile
  mkdocs.yml
  README.md
```

## Current Status

The current scaffold already includes:

- project identity and documentation
- FastAPI backend with modular domain routes
- React frontend shell with operator-focused pages
- Docker Compose workflow for backend, frontend, and PostgreSQL
- reusable folders for IoT and applied AI domains

## Engine Integration Modes

The frontend always calls the backend API.

This repository now supports two runtime patterns:

1. `embedded`
   The runtime lives inside the backend process.
2. `external`
   A Python, C++, or any other runtime pushes data into backend ingest endpoints while the frontend still talks only to the backend.

Key routes:

- `GET /api/v1/engine/status`
- `POST /api/v1/ingest/devices`
- `POST /api/v1/ingest/telemetry`
- `POST /api/v1/ingest/ai-events`
- `POST /api/v1/ingest/inspections`

## Quick Start

### 1. Create the environment file

```powershell
Copy-Item .env.example .env
```

### 2. Start the local stack

```bash
make dev
```

### 3. Open the services

- frontend: `http://localhost:5173`
- backend: `http://localhost:8000`
- API docs: `http://localhost:8000/docs`
- docs site: `python -m mkdocs serve`

## Quality And CI

Local quality checks:

```bash
make ci-local
```

CI is defined in `.github/workflows/ci.yml` and validates:

- backend lint
- backend tests
- frontend build
- docs build
- Docker Compose configuration

## Deployment

The repository includes a Render starter in `render.yaml`.

That starter is intended as a first deployment path for:

- backend web service
- frontend static site

Production deployment still needs:

- managed PostgreSQL
- real auth and secrets
- database-backed services instead of bootstrap sample data
- final domain and CORS configuration

## Next Steps

1. Replace bootstrap sample data with database-backed services.
2. Add authentication flows and role-aware actions.
3. Expand device, telemetry, event, and inspection workflows.
4. Add typed mutations, tests, and realtime streams.

## Documentation

Project docs live in `docs/`.

- [Docs home](docs/index.md)
- [Getting started](docs/getting-started.md)
- [Architecture](docs/architecture.md)
- [Engine integration](docs/engine-integration.md)
- [Backend](docs/backend.md)
- [Frontend](docs/frontend.md)
- [Deployment](docs/deployment.md)
