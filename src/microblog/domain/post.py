from datetime import datetime


class Post:
    def __init__(self, id: int, blog_id: int, author_id: int, title: str, content: str, created_at: datetime, updated_at: datetime):
        self.id = id
        self.blog_id = blog_id
        self.author_id = author_id
        self.title = title
        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at
