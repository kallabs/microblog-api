import logging

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from microblog.services import post_service, unit_of_work
from microblog.services.auth import get_current_user, User

logger = logging.getLogger(__name__)
router = APIRouter()


class CreatePostRequest(BaseModel):
    title: str
    content: str


@router.post("/posts/")
async def create_post(
    data: CreatePostRequest,
    user: User = Depends(get_current_user),
):
    logger.debug(data, user)
    post_in = post_service.CreatePostInput(**data, author_id=user.id)
    uow = unit_of_work.AlchemyUnitOfWork()
    post = await post_service.create_post(post_in=post_in, uow=uow)
    
    return post


@router.get("/posts/")
async def list_posts(user: User = Depends(get_current_user)):
    print(user)
    return []