# Backend

The backend will expose modular API routes for operational domains instead of a single generic dashboard endpoint.

## Initial backend domains

- auth
- devices
- telemetry
- ai-events
- inspections

## Shape

- FastAPI application entry point
- route modules grouped by domain
- service layer for business logic
- SQLAlchemy models and session helpers
- Pydantic schemas for request and response contracts
