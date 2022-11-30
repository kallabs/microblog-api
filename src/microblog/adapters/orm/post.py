import datetime as dt

from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from .db import Base
from .blog import Blog


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
