from fastapi import HTTPException, status

from database import user_collection
from schemas import LoginRequest
from utils.security import (
    verify_password,
    create_access_token
)


async def login_user(
    login_data: LoginRequest
):
    user = await user_collection.find_one({
        "username": login_data.username
    })
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    
    password_valid = verify_password(
        login_data.password,
        user["password"]
    )

    if not password_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        username=user["username"],
        role=user["role"]
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user["username"],
        "role": user["role"]
    }