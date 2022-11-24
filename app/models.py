import datetime as dt

from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from .db import Base


class DateTimeMixin:
    """Datetime mixin to add created_at & updated_at columns if needed."""

    created_at = Column(DateTime, default=dt.datetime.utcnow)
    updated_at = Column(DateTime, default=dt.datetime.now, onupdate=dt.datetime.now)


class Blog(Base, DateTimeMixin):
    __tablename__ =  'blogs'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer)
    title = Column(String(256))
    desc = Column(String())

    posts = relationship("Post", back_populates="Post")


class Post(Base, DateTimeMixin):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    blog_id = Column(Integer, ForeignKey(f"{Blog.__table__.name}.id"))
    author_id = Column(Integer)
    title = Column(String(265))
    content = Column(Text)
    
    blog = relationship("Blog", back_populates="posts")
