import abc

from microblog.app.gateways.post import AbstractPostGateway


class AbstractUnitOfWork(abc.ABC):
    posts: AbstractPostGateway

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
