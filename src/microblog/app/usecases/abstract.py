import abc

from microblog.app.unit_of_work import AbstractUnitOfWork


class AbstractUseCase(abc.ABC):
    def __init__(self, uow: AbstractUnitOfWork) -> None:
        self.uow = uow