from pydantic import BaseModel, EmailStr


# -------- REQUEST SCHEMAS --------
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# -------- RESPONSE SCHEMAS (optional but good practice) --------
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str








