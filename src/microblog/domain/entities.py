from __future__ import annotations

from datetime import datetime
from enum import Enum


class Tag:
    def __init__(self, *, id: int, name: str):
        self.id = id
        self.name = name

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        self._name = value


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
    
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, value: str) -> None:
        self._email = value

    @property
    def first_name(self) -> str:
        return self._first_name
    
    @first_name.setter
    def first_name(self, value: str) -> None:
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name
    
    @last_name.setter
    def last_name(self, value: str) -> None:
        self._last_name = value


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
        tags: list[Tag] = list,
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

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def author_id(self) -> int:
        return self._author_id
    
    @author_id.setter
    def author_id(self, value: int) -> None:
        self._author_id = value

    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    @property
    def content(self) -> str:
        return self._content
    
    @content.setter
    def content(self, value: str) -> None:
        self._content = value

    @property
    def status(self) -> PostStatus:
        return self._status

    @status.setter
    def status(self, value: PostStatus) -> None:
        self._status = value

    @property
    def slug(self) -> str:
        return self._slug

    @slug.setter
    def slug(self, value: str) -> None:
        self._slug = value

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @created_at.setter
    def created_at(self, value: datetime) -> None:
        self._created_at = value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value: datetime) -> None:
        self._updated_at = value

    @property
    def published_at(self) -> datetime:
        return self._published_at

    @published_at.setter
    def published_at(self, value: datetime) -> None:
        self._published_at = value

    @property
    def tags(self) -> list[Tag]:
        return self._tags
    
    @tags.setter
    def tags(self, tags: list[Tag]) -> None:
        self._tags = tags

    @property
    def author(self) -> Author:
        return self._author
    
    @author.setter
    def author(self, value: Author) -> None:
        self._author = value

    def publish(self):
        """Makes the post available for other users"""
        self.status = PostStatus.published
        self.published_at = datetime.now()