from __future__ import annotations

import logging

from sqlalchemy import select

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
                               content=post.content)
        self.session.add(post_obj)
        await self.session.commit()

        return post_obj
    
    async def get(self, id: int) -> Post:
        query = select(models.Post)\
            .filter_by(id=id)\
            .first()
        result = await self.session.execute(query)
        return result.scalars().one()

    async def list(self) -> list[Post]:
        query = select(models.Post)
        result = await self.session.execute(query)
        
        return result.fetchall()