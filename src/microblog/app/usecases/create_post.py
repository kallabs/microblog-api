import abc
from dataclasses import dataclass

from microblog.domain.entities import Post
from microblog.app.unit_of_work import AbstractUnitOfWork
from microblog.app.usecases.exceptions import TitleAlreadyExists
from microblog.app.gateways.utils import AbstractUtilsGateway
from microblog.app.gateways.exceptions import PersistSaveError


@dataclass(frozen=True)
class CreatePostInputModel:
    author_id: int
    title: str
    content: str


class CreatePostInputPort(abc.ABC):
    @abc.abstractmethod
    def __call__(self, input_model: CreatePostInputModel) -> Post: ...


class CreatePostInteractor(CreatePostInputPort):
    """
    Steps:
    1. Initialize Post entity by using input model data
    2. Check if posts with such title already exist, if so - raise TitleAlreadyExists
    3. If not than pass entity to create post gateway
    """
    def __init__(self, uow: AbstractUnitOfWork, utils: AbstractUtilsGateway) -> None:
        self._uow = uow
        self._utils = utils
    
    async def __call__(self, input_model: CreatePostInputModel) -> Post:
        
        new_post = Post(
            author_id=input_model.author_id,
            title=input_model.title,
            content=input_model.content,
            slug=self._utils.slugify(input_model.title))
        
        async with self._uow as uow:
            title_exists = await uow.posts.has_such_title(input_model.title)
                
            if title_exists:
                raise TitleAlreadyExists
            
            try:
                new_post = await uow.posts.create(new_post)
            except PersistSaveError:
                raise PersistSaveError
            
            await uow.commit()

        return new_post