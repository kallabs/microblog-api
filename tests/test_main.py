import pytest

from microblog.main import app

pytestmark = pytest.mark.anyio


async def test_root(client):
    response = await client.get("/")
    assert response.status_code == 200


async def test_blogs_create(client):
    response = await client.post("/blogs/")
    assert response.status_code == 200
    assert response.json() == {'action': 'Blog create'}


async def test_posts_create(client):
    response = await client.post("/posts/")
    print(response.headers)
    assert response.status_code == 200
    assert response.json() == {'action': 'Post create'}

async def test_simple():
    assert 'x' == 'x'