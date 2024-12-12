from pydantic import BaseModel, Field, EmailStr, PastDate, ConfigDict
from datetime import datetime
from typing import List, Optional


class ContactModel(BaseModel):
    firstname: str = Field(max_length=50)
    lastname: str = Field(max_length=50)
    email: str = EmailStr()
    phone: str = Field(max_length=50)
    birthdate: datetime = PastDate()
    additional: Optional[str] = None


class ContactResponse(ContactModel):
    id: int


class User(BaseModel):
    id: int
    username: str
    email: str
    avatar: str

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class RequestEmail(BaseModel):
    email: EmailStr
