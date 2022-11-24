from fastapi import APIRouter, Request

router = APIRouter(prefix="/blogs")


@router.post("/")
async def create(
    request: Request,
) -> None:
    return {'action': 'Blog create'}
