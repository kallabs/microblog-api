from abc import abstractmethod

from .base import AbstractRepo

class AbstractBlogRepo(AbstractRepo):
    @abstractmethod
    def get(self):
        raise NotImplementedError