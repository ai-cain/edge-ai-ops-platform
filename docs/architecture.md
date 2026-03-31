# Architecture

## Guiding principles

- frontend-first product thinking
- modular backend domains
- typed contracts
- realtime-ready infrastructure
- clean handoff from local dev to production

## Domain areas

- auth
- devices
- telemetry
- ai-events
- inspections
- alerts
- dashboards
- settings

## Planned structure

```text
backend/
  app/
    api/
    core/
    models/
    schemas/
    services/

frontend/
  src/
    app/
    components/
    features/
    routes/
    lib/
```

## Active backend routes

- `/api/v1/health`
- `/api/v1/auth/status`
- `/api/v1/auth/token`
- `/api/v1/devices`
- `/api/v1/telemetry/latest`
- `/api/v1/ai-events`
- `/api/v1/inspections`
