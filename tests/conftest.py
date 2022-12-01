import pytest
from httpx import AsyncClient

from microblog.entrypoints.app import app


@pytest.fixture
def anyio_backend():
    return 'asyncio'
    

@pytest.fixture
async def client():
    async with AsyncClient(
        app=app, 
        base_url="http://localhost:8008",
        headers={"Content-Type": "application/json"}
    ) as client:
        yield client