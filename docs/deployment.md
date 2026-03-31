# Deployment

This repository now includes a simple deployment starter for Render.

## Current deployment assets

- `render.yaml` for a backend web service and frontend static site
- Dockerfiles for backend and frontend
- GitHub Actions CI for backend, frontend, docs, and Compose validation

## Render starter shape

- backend deploys from `backend/Dockerfile`
- frontend deploys as a static Vite build from `frontend/`
- `DATABASE_URL` is expected as a managed secret

## Before first production deploy

- replace bootstrap sample services with database-backed logic
- set production CORS origins
- attach a managed PostgreSQL instance
- add real auth and secret management
- verify websocket strategy for your hosting target

## CI

The GitHub Actions workflow validates:

- backend lint
- backend tests
- frontend build
- docs build
- Docker Compose configuration
