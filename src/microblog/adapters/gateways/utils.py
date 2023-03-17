from __future__ import annotations

import logging

from slugify import slugify

from microblog.app.gateways.utils import AbstractUtilsGateway

logger = logging.getLogger(__name__)


class UtilsGateway(AbstractUtilsGateway):
    def slugify(self, line: str) -> str:
        return slugify(line)