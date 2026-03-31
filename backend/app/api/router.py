from fastapi import APIRouter

from app.api.routes import ai_events, auth, devices, health, inspections, telemetry

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(devices.router)
api_router.include_router(telemetry.router)
api_router.include_router(ai_events.router)
api_router.include_router(inspections.router)
