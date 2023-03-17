from __future__ import annotations

import abc


class AbstractUtilsGateway(abc.ABC):
    @abc.abstractmethod
    def slugify(self, line: str) -> str: ...