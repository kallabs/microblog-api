from __future__ import annotations

import logging

from fastapi import APIRouter, Depends

from microblog.domain.entities import Post
from microblog.app.usecases.exceptions import TitleAlreadyExists
from microblog.app.usecases.create_post import CreatePostInteractor, CreatePostInputModel
from microblog.app.usecases.list_posts import ListPostsInputModel, ListPostsInteractor
from .auth import get_current_user, User
from .gateways.utils import UtilsGateway
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
    utils_gateway = UtilsGateway()
    interactor = CreatePostInteractor(uow, utils_gateway)
    
    try:
        post = await interactor(input_model)
    except TitleAlreadyExists:
        return {
            'data': None,
            'errors': 'Such title already exists'
        }
    
    return {
        'data': post,
        'errors': None,
    }


@router.get("/posts/")
async def list_posts(
    user: User = Depends(get_current_user),
) -> list[Post]:
    
    uow = AlchemyUnitOfWork()
    input_model = ListPostsInputModel(user_id=user.id)
    logger.debug(user, uow, input_model)
    interactor = ListPostsInteractor(uow)
    posts = await interactor(input_model)

    return {
        'data': posts,
        'errors': None,
    }