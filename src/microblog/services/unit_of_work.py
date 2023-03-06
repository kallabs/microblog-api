import abc

from microblog.adapters.orm.db import async_session
from microblog.adapters.repos.abstract import AbstractPostRepo
from microblog.adapters.repos.sqlalchemy.post import AlchemyPostRepo


class AbstractUnitOfWork(abc.ABC):
    posts: AbstractPostRepo

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class AlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=async_session):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.posts = AlchemyPostRepo(self.session)
        
    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
