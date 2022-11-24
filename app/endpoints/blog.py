from fastapi import APIRouter, Depends, Path, Request

router = APIRouter(prefix="/blogs")


@router.post("/")
async def create(
    request: Request,
) -> None:
    return {'action': 'Blog create'}
