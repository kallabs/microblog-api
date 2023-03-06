from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from microblog.adapters.orm.db import get_session
from microblog.services.auth import get_current_user, User
from microblog.services import post_service, unit_of_work

router = APIRouter()


@router.post("/posts/")
async def create_post(
    user: User = Depends(get_current_user),
):
    print(user)
    uow = unit_of_work.AlchemyUnitOfWork()
    post = await post_service.create_post(author_id=user.id,
                                    title='Title',
                                    content='Content',
                                    uow=uow)
    return post

@router.get("/posts/")
async def list_posts(user: User = Depends(get_current_user)):
    print(user)
    return []