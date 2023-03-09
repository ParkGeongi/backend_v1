
from typing import List, Optional

from pydantic import BaseModel


class ClothDTO(BaseModel):
    cloth_id: Optional[int]
    name: Optional[str]
    brand: Optional[str]
    gender: Optional[str]
    price: Optional[str]
    category: Optional[str]
    cloth_img: Optional[str]
    color: Optional[str]


    class Config:
        orm_mode = True


