from datetime import datetime


class Blog:
    def __init__(self, id: int, owner_id: int, title: str, desc: str, created_at: datetime, updated_at: datetime, posts: list = list):
        self.id = id
        self.owner_id = owner_id
        self.title = title
        self.desc = desc
        self.created_at = created_at
        self.updated_at = updated_at
        self.posts = []