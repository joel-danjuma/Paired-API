from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# ROOMMATE_ADS
class RoommateAd(BaseModel):
    id: int
    gender: str
    budget: int
    pets: bool
    smoking: bool
    available_from: str
    owner_id: int
    created_at: datetime


class CreateRoommateAd(BaseModel):
    gender: str
    budget: str
    pets: bool
    smoking: bool
    available_from: str


# USERS
class UserBase(BaseModel):
    email: EmailStr
    password: str


class CreateUser(UserBase):
    pass


class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UpdateUserPassword(BaseModel):
    password: str


class UpdateUserEmail(BaseModel):
    email: EmailStr


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ROOM_ADS
class CreateRoomAd(BaseModel):
    location: str
    price: int
    bedrooms: int
    smoking: bool
    pets: bool
    available_from: str

    class config:
        orm_mode = True


# AUTH
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str = None
