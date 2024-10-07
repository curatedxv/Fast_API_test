from fastapi import *
from pydantic import *
from typing import *
from enum import *
from fastapi_users import fastapi_users
from fastapi_users import FastAPIUsers
from auth.auth import auth_backend
from auth.shemes import UserRead, UserCreate
from auth.manager import get_user_manager, User

app = FastAPI(
    title="Trading App"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_auth_router(UserRead, UserCreate),
    prefix="/auth/jwt",
    tags=["auth"],
)
