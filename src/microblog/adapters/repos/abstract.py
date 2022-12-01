from abc import ABC, abstractmethod
from microblog.domain.blog import Blog


class AbstractRepo(ABC):
    ...


class AbstractBlogRepo(AbstractRepo):
    @abstractmethod
    def get(self, id: int) -> Blog:
        raise NotImplementedError