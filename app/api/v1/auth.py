from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr

from app.repositories.user_repository import (
    get_user_by_email,
    create_user
)
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest):
    if len(payload.password.encode("utf-8")) > 72:
        raise HTTPException(
            status_code=422,
            detail="Password too long"
        )

    if get_user_by_email(payload.email):
        raise HTTPException(status_code=409, detail="Email already registered")

    user = create_user(
        email=payload.email,
        hashed_password=hash_password(payload.password)
    )

    return {
        "id": user["id"],
        "email": user["email"],
        "created_at": user["created_at"]
    }


@router.post("/login")
def login(payload: LoginRequest):
    user = get_user_by_email(payload.email)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(payload.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return create_access_token(user["id"])
