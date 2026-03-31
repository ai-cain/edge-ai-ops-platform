from fastapi import APIRouter

from app.schemas.auth import AuthStatus, TokenRequest, TokenResponse
from app.services.auth_service import get_auth_status, issue_access_token


router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/status", response_model=AuthStatus)
async def read_auth_status() -> AuthStatus:
    return get_auth_status()


@router.post("/token", response_model=TokenResponse)
async def create_token(payload: TokenRequest) -> TokenResponse:
    return issue_access_token(payload)
