from __future__ import annotations

import logging

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import joinedload, selectinload

from microblog.app.gateways.exceptions import PersistSaveError
from microblog.app.gateways.post import AbstractPostGateway
from microblog.domain.entities import Post
from microblog.adapters.persistence import models

logger = logging.getLogger(__name__)


class AlchemyPostGateway(AbstractPostGateway):
    def __init__(self, session):
        self.session = session

    async def create(self, post: Post) -> Post:
        logger.debug(post.__dict__)
        post_obj = models.Post(author_id=post.author_id,
                               title=post.title,
                               content=post.content,
                               slug=post.slug,
                               status=post.status.value)
        self.session.add(post_obj)
        
        try:
            await self.session.commit()
        except IntegrityError as e:
            raise PersistSaveError(str(e))

        return post_obj
    
    async def get(self, id: int) -> Post:
        query = select(models.Post)\
            .filter_by(id=id)\
            .first()
        result = await self.session.execute(query)
        obj = result.scalars().one()
        
        return obj

    async def list(self) -> list[Post]:
        query = select(models.Post)\
            .options(selectinload(models.Post.tags))
        result = await self.session.execute(query)
        result = result.scalars().all()

        return result
    
    async def has_such_title(self, title: str) -> bool:
        query = select(models.Post.id).filter_by(title=title)
        result = await self.session.execute(query)
        
        return result.first() is not None