from pydantic import BaseModel
from uuid import UUID,uuid4
from typing import Optional
from enum import Enum


class Gender(str,Enum):

    male="male"
    femail="femail"

class User(BaseModel):
    id: UUID = uuid4()
    username: str
    email: str
    gender: Gender
    