from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None
    picture_url: Optional[str] = None


class UserCreate(UserBase):
    google_id: str


class User(UserBase):
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ProjectBase(BaseModel):
    project_name: str


class ProjectCreate(ProjectBase):
    owner_id: int


class Project(ProjectBase):
    project_id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime
    owner: User

    class Config:
        from_attributes = True
