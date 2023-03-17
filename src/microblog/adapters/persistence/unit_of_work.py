import abc
import asyncio

from microblog.adapters.persistence.db import async_session
from microblog.adapters.gateways.post import AlchemyPostGateway
from microblog.app.unit_of_work import AbstractUnitOfWork


class AlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=async_session):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()
        self.posts = AlchemyPostGateway(self.session)
        await asyncio.sleep(0.5)

        return self
        
    async def __aexit__(self, *args):
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
