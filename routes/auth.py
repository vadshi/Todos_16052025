from typing import Annotated, AsyncIterator
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models import Users
from schemas import CreateUserRequest, UserDB, UserLogin, UserResponse
from passlib.context import CryptContext
from dataclasses import dataclass

import bcrypt


@dataclass
class SolveBugBcryptWarning:
    __version__: str = getattr(bcrypt, "__version__")


setattr(bcrypt, "__about__", SolveBugBcryptWarning())


router = APIRouter()


SECRET_KEY = '259eedaa93c111c0370f5a166cf7b3548ddf977cfd2de488bfde7fb47eea46b9'
ALGORITM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

db_dependency = Annotated[AsyncIterator[AsyncSession], Depends(get_db)]


@router.post("/register", status_code=201)
async def create_user(
        session: db_dependency, 
        user_data: CreateUserRequest = Body()
    ) -> UserResponse:
    user_dict = user_data.model_dump()
    password = user_dict.pop('password')
    user_dict["hashed_password"] = bcrypt_context.hash(password)
    user_model = Users(**user_dict)
    session.add(user_model)
    await session.commit()
    await session.refresh(user_model)

    new_user = UserDB.model_validate(user_model)
    resp_user = new_user.model_dump()
    return resp_user
   

@router.post("/login", status_code=200, response_model=UserResponse)
async def login_user(
        session: db_dependency, 
        user_data: UserLogin = Body()
    ):
    query = select(Users).filter(Users.username == user_data.username)
    result = await session.execute(query)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(404, f"User with username: {user_data.username} not found.")
    if not bcrypt_context.verify(user_data.password, user.hashed_password):
        raise HTTPException(400, f"Wrong username or password.")

    new_user = UserDB.model_validate(user)
    resp_user = new_user.model_dump()
    return resp_user
   