import datetime as dt

from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base
from app.shared.mixins import DateTimeMixin
from app.blog.models import Blog


class Post(Base, DateTimeMixin):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    blog_id = Column(Integer, ForeignKey(f"{Blog.__table__.name}.id"))
    author_id = Column(Integer)
    title = Column(String(265))
    content = Column(Text)
    
    blog = relationship("Blog", back_populates="posts")
