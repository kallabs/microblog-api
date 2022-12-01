import pytest

pytestmark = pytest.mark.anyio


async def test_root(client):
    response = await client.get("/")
    assert response.status_code == 200
