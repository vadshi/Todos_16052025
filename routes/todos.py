
from typing import Annotated
from schemas import UserResponse
from fastapi import Depends

from routes.auth import login_user

# Пользователь, который прошел аутентификацию и может создавать задачи.
user_dependency = Annotated[UserResponse, Depends(login_user)]