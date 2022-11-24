from fastapi import APIRouter, Request

router = APIRouter(prefix="/posts")


@router.post("/")
async def create(
    request: Request,
) -> None:
    return {'action': 'Post create'}
