from microblog.services.unit_of_work import AbstractUnitOfWork
from microblog.domain.entities import Post


def create_post(
    author_id: int, title: str, content: str, 
    uow: AbstractUnitOfWork
) -> Post:
    new_post = Post(
        author_id=author_id,
        title=title,
        content=content,
    )
    with uow:
        new_post = uow.posts.create(new_post)
        uow.commit()

    return new_post