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

This repository is being scaffolded as a reusable base. The first milestone sets up:

- project identity and documentation
- backend and frontend app skeletons
- local Docker workflow
- modular folders for IoT and applied AI domains

## Next Steps

1. Scaffold backend modules and API surface.
2. Scaffold frontend shell and domain pages.
3. Wire Docker-based local development.
4. Add typed API contracts, tests, and docs.

## Documentation

Project docs live in `docs/`.

- [Docs home](docs/index.md)
- [Getting started](docs/getting-started.md)
- [Architecture](docs/architecture.md)
- [Backend](docs/backend.md)
- [Frontend](docs/frontend.md)
