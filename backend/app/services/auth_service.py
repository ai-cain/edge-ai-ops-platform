from app.schemas.auth import AuthStatus, TokenRequest, TokenResponse


def get_auth_status() -> AuthStatus:
    return AuthStatus(
        mode="bootstrap",
        provider="api-key",
        notes="Authentication is scaffolded and ready for JWT or SSO integration.",
    )


def issue_access_token(payload: TokenRequest) -> TokenResponse:
    masked_suffix = payload.api_key[-4:]
    return TokenResponse(
        access_token=f"bootstrap-token-{masked_suffix}",
        expires_in_seconds=3600,
    )
