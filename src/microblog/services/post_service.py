from pydantic import BaseModel, Field

from microblog.services.unit_of_work import AbstractUnitOfWork
from microblog.domain.entities import Post


class CreatePostInput(BaseModel):
    author_id: int
    title: str
    content: str


async def create_post(
    post_in: CreatePostInput,
    uow: AbstractUnitOfWork
) -> Post:
    new_post = Post(
        author_id=post_in.author_id,
        title=post_in.title,
        content=post_in.content,
    )
    with uow:
        new_post = await uow.posts.create(new_post)
        await uow.commit()

    return new_post