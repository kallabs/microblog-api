import datetime as dt

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base
from app.shared.mixins import DateTimeMixin


class Blog(Base, DateTimeMixin):
    __tablename__ =  'blogs'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer)
    title = Column(String(256))
    desc = Column(String())

    posts = relationship("Post", back_populates="Post")
