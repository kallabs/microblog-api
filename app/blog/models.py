import datetime as dt

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class Blog(Base):
    __tablename__ =  'blogs'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    owner_id = Column(Integer, index=True, nullable=False)
    title = Column(String(256), nullable=False)
    desc = Column(String(512))
    created_at = Column(DateTime, default=dt.datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=dt.datetime.now, onupdate=dt.datetime.now, nullable=False)

    posts = relationship("Post", back_populates="Post")
