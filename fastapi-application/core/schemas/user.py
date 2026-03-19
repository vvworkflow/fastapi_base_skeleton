from pydantic import BaseModel


class User(BaseModel):
    username: str


class UserCreate(User):
    password: str


class UserRead(User):
    pass
