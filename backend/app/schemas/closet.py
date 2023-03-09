
from typing import List, Optional

from pydantic import BaseModel


class ClosetDTO(BaseModel):
    closet_id: Optional[int]
    cloth_img: Optional[str]
    user_id: Optional[str]
    cloth_id: Optional[str]

    class Config:
        orm_mode = True


