from pydantic import BaseModel, Field


class AuthStatus(BaseModel):
    mode: str
    provider: str
    notes: str


class TokenRequest(BaseModel):
    api_key: str = Field(min_length=8)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in_seconds: int
