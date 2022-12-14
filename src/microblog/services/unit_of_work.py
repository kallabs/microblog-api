import abc

from microblog.adapters.orm.db import async_session
from microblog.adapters.repos.abstract import AbstractBlogRepo
from microblog.adapters.repos.sqlalchemy.blog import AlchemyBlogRepo


class AbstractUnitOfWork(abc.ABC):
    blogs: AbstractBlogRepo

    def __exit__(self):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError



class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=async_session):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.blogs = AlchemyBlogRepo(self.session)
        
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
