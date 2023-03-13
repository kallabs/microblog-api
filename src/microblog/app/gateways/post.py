from __future__ import annotations

import abc

from microblog.domain.entities import Post


class AbstractPostGateway(abc.ABC):
    @abc.abstractmethod
    def create(self, post: Post) -> Post: ...
    
    @abc.abstractmethod
    def get(self, id: int) -> Post: ...

    @abc.abstractmethod
    def list(self) -> list[Post]: ...
