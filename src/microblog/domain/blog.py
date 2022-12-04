from __future__ import annotations
from datetime import datetime

from .post import Post


class Blog:
    def __init__(self, id: int, owner_id: int, title: str, desc: str, created_at: datetime, updated_at: datetime, posts: list = list):
        self.id = id
        self.owner_id = owner_id
        self.title = title
        self.desc = desc
        self.created_at = created_at
        self.updated_at = updated_at
        self.set_posts(posts)
    
    def set_posts(self, posts: list[Post]) -> None:
        self.posts = posts
