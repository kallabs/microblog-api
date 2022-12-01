from ..abstract import AbstractBlogRepo
from microblog.domain.blog import Blog


class AlchemyBlogRepo(AbstractBlogRepo):
    def __init__(self, session):
        self.session = session

    def get(self, id: int) -> Blog:
        return None