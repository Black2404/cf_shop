from fastapi import APIRouter

from schemas import LoginRequest, LoginResponse
from services.auth_service import login_user

from fastapi import APIRouter, Depends

from schemas import LoginRequest, LoginResponse
from services.auth_service import login_user
from utils.dependencies import get_current_user, require_admin


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=LoginResponse)
async def login(login_data: LoginRequest):
    return await login_user(login_data)

