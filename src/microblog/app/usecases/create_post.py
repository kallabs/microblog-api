import abc
from dataclasses import dataclass

from microblog.domain.entities import Post
from microblog.app.unit_of_work import AbstractUnitOfWork


@dataclass(frozen=True)
class CreatePostInputModel:
    author_id: int
    title: str
    content: str


class CreatePostInputPort(abc.ABC):
    @abc.abstractmethod
    def __call__(self, input_model: CreatePostInputModel) -> Post: ...


class CreatePostInteractor(CreatePostInputPort):
    def __init__(self, uow: AbstractUnitOfWork) -> None:
        self._uow = uow
    
    async def __call__(self, input_model: CreatePostInputModel) -> Post:
        
        new_post = Post(
            author_id=input_model.author_id,
            title=input_model.title,
            content=input_model.content)
        
        async with self._uow as uow:
            new_post = await uow.posts.create(new_post)
            await uow.commit()

        return new_post