from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Cloth(Base):
    __tablename__ = 'closet'
    cloth_id = Column(String(30), primary_key=True)
    name = Column(String(30))
    brand = Column(String(30))
    gender = Column(String(30))
    price = Column(String(30))
    category = Column(String(30))
    img = Column(String(100))
    color = Column(String(30))


    closets = relationship('Closet', back_populates='cloth')

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'아아디: {self.closet_id}, \n ' \
               f'이미지: {self.cloth_img} \n'