from abc import ABC, abstractmethod
from microblog.domain.entities import Post


class AbstractRepo(ABC):
    ...


class AbstractPostRepo(AbstractRepo):
    @abstractmethod
    def create(self, post: Post) -> Post:
        raise NotImplementedError
    
    @abstractmethod
    def get(self, id: int) -> Post:
        raise NotImplementedError
