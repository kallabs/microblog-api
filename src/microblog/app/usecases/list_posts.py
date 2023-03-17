from __future__ import annotations

import abc
import logging
from dataclasses import dataclass

from microblog.domain.entities import Post
from microblog.app.unit_of_work import AbstractUnitOfWork

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ListPostsInputModel:
    user_id: int


class ListPostsInputPort(abc.ABC):
    @abc.abstractmethod
    def __call__(self, input_model: ListPostsInputModel) -> list[Post]:
        ...


class ListPostsInteractor(ListPostsInputPort):
    def __init__(self, uow: AbstractUnitOfWork) -> None:
        self._uow = uow
    
    async def __call__(self, input_model: ListPostsInputModel) -> list[Post]:
        async with self._uow as uow:
            posts = await uow.posts.list()

        return posts