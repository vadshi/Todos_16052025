from pydantic import BaseModel, ConfigDict, Field


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool = False

class BaseUser(BaseModel):
    email: str
    username: str
    first_name: str | None = None
    last_name: str | None = None
    is_active: bool = True
    role: str | None = None
    phone_number: str | None = None
    
class CreateUserRequest(BaseUser):
    password: str 
  

class UserResponse(BaseUser):
    model_config = ConfigDict(from_attributes=True)
    id: int

class UserLogin(BaseModel):
    username: str
    password: str