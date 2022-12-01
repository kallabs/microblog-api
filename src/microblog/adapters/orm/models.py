import datetime as dt

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .db import Base


class Blog(Base):
    __tablename__ =  'blogs'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    owner_id = Column(Integer, index=True, nullable=False)
    title = Column(String(256), nullable=False)
    desc = Column(String(512))
    created_at = Column(DateTime, default=dt.datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=dt.datetime.now, onupdate=dt.datetime.now, nullable=False)
    
    posts = relationship("Post", back_populates="Post")


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    blog_id = Column(Integer, ForeignKey(f"{Blog.__table__.name}.id"), nullable=False, index=True)
    author_id = Column(Integer, nullable=False, index=True)
    title = Column(String(265), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=dt.datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=dt.datetime.now, onupdate=dt.datetime.now, nullable=False)
    
    blog = relationship("Blog", back_populates="posts")
