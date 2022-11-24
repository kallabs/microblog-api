
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (
    "mysql+aiomysql://{user}:{password}@{host}/{db}?host=localhost?port={port}".format(
        user=os.environ['MARIADB_USER'],
        password=os.environ['MARIADB_PASSWORD'],
        host=os.environ['MARIADB_HOST'],
        port=os.environ['MARIADB_PORT'],
        db=os.environ['MARIADB_DATABASE'],
    )
)

engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
