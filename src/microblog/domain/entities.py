from typing import List
from datetime import datetime
from enum import Enum


class Tag:
    def __init__(self, *, id: int, name: str):
        self.id = id
        self.name = name


class PostStatus(Enum):
    draft = 0
    published = 1
    deleted = 2


class Author:
    def __init__(
        self, *,
        id: int, 
        email: str,
        first_name: str,
        last_name: str
    ) -> None:
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name


class Post:
    def __init__(
        self, *,
        id: int = None, 
        author_id: int,
        title: str, 
        content: str,
        slug: str = None,
        created_at: datetime = None, 
        updated_at: datetime = None, 
        published_at: datetime = None,
        status: PostStatus = PostStatus.draft,
        tags: List[Tag] = list,
        author: Author = None
    ):
        self.id = id
        self.author_id = author_id
        self.title = title
        self.content = content
        self.status = status
        self.slug = slug
        self.created_at = created_at
        self.updated_at = updated_at
        self.published_at = published_at
        self.status = status
        self.tags = tags
        self.author = author

    def publish(self):
        """Makes the post available for other users"""
        self.status = PostStatus.published
        self.published_at = datetime.now()