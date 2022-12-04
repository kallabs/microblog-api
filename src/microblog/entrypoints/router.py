from fastapi import APIRouter

router = APIRouter()


@router.get("/blogs/", tags=["blogs"])
async def list_blogs():
    return []