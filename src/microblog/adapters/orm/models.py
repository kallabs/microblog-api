import datetime as dt

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, mapper
from sqlalchemy.schema import UniqueConstraint

from .db import Base


class PostTag(Base):
    __tablename__ = "post_tag"

    post_id = Column(Integer, ForeignKey('posts.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)


class Tag(Base):
    __tablename__ =  'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    posts = relationship('Post', secondary='post_tag', back_populates='tags')

    def __repr__(self):
        return f'<Tag "{self.name}">' 


class Post(Base):
    __tablename__ = 'posts'
    __table_args__ = (UniqueConstraint('author_id', 'title', name='ux_author_title'), )

    id = Column(Integer, primary_key=True, index=True, unique=True)
    author_id = Column(Integer, nullable=False, index=True)
    title = Column(String(255), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    slug = Column(String(255), nullable=False)
    status = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=dt.datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=dt.datetime.now, onupdate=dt.datetime.now, nullable=False)
    published_at = Column(DateTime, nullable=True)
    
    tags = relationship('Tag', secondary='post_tag', back_populates='posts')
