from __future__ import annotations

from typing import List
import datetime as dt

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.schema import UniqueConstraint

from microblog.domain import entities
from .db import Base


class PostTag(Base):
    __tablename__ = "post_tag"

    post_id = Column(Integer, ForeignKey('posts.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)


class Tag(Base):
    __tablename__ =  'tags'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    posts: Mapped[List['Post']] = relationship('Post', secondary='post_tag', back_populates='tags')

    def __repr__(self):
        return f'<Tag "{self.name}">' 


class Post(Base):
    __tablename__ = 'posts'
    __table_args__ = (UniqueConstraint('author_id', 'title', name='ux_author_title'), )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, unique=True)
    author_id: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    slug: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.utcnow, nullable=False)
    updated_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.now, onupdate=dt.datetime.now, nullable=False)
    published_at: Mapped[dt.datetime] = mapped_column(DateTime, nullable=True)
    
    tags: Mapped[List['Tag']] = relationship('Tag', secondary='post_tag', back_populates='posts')
