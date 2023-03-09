from datetime import datetime
from typing import List, Optional, Any
from uuid import UUID
from pydantic import BaseModel


class UserDTO(BaseModel):
    user_id: Optional[str]
    email: Optional[str]
    password: Optional[str]
    name: Optional[str]
    phone: Optional[str]
    token: Optional[str]



    class Config:
        orm_mode = True

