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

## Current scaffold routes

- health
- auth
- engine
- devices
- telemetry
- ai-events
- inspections
- ingest

## Runtime strategy

The backend supports two patterns:

- embedded runtime mode
- external runtime mode for Python, C++, or any other language

That keeps the frontend contract stable while letting the engine implementation vary.
