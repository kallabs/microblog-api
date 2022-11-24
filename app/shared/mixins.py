import datetime as dt

from sqlalchemy import Column, DateTime


class DateTimeMixin:
    """Datetime mixin to add created_at & updated_at columns if needed."""

    created_at = Column(DateTime, default=dt.datetime.utcnow)
    updated_at = Column(DateTime, default=dt.datetime.now, onupdate=dt.datetime.now)
