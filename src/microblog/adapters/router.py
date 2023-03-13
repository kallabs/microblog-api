from __future__ import annotations

import logging

from fastapi import APIRouter, Depends

from microblog.domain.entities import Post
from microblog.app.usecases.create_post import CreatePostInteractor, CreatePostInputModel
from microblog.app.usecases.list_posts import ListPostsInputModel, ListPostsInteractor
from .auth import get_current_user, User
from .persistence.unit_of_work import AlchemyUnitOfWork
from .schemas import CreatePostRequest

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/posts/")
async def create_post(
    data: CreatePostRequest,
    user: User = Depends(get_current_user),
):
    logger.debug(data, user)
    uow = AlchemyUnitOfWork()
    input_model = CreatePostInputModel(
        author_id=user.id,
        title=data.title,
        content=data.content)
    
    interactor = CreatePostInteractor(uow)
    post = await interactor(input_model)
    
    return post


@router.get("/posts/")
async def list_posts(
    user: User = Depends(get_current_user),
) -> list[Post]:
    
    uow = AlchemyUnitOfWork()
    input_model = ListPostsInputModel(user_id=user.id)
    logger.debug(user, uow, input_model)
    interactor = ListPostsInteractor(uow)
    posts = await interactor(input_model)

    return posts