import logging

from ..abstract import AbstractPostRepo
from microblog.domain.entities import Post
from microblog.adapters.orm import models

logger = logging.getLogger(__name__)


class AlchemyPostRepo(AbstractPostRepo):
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
    
    def get(self, id: int) -> Post:
        return self.session.query(models.Post)\
            .filter_by(id=id)\
            .first()

    