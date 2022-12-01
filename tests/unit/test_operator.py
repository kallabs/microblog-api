import pytest

pytestmark = pytest.mark.anyio

async def test_simple():
    assert 'x' == 'x'