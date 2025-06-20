from fastapi import APIRouter


router = APIRouter(tags=["hello"])


@router.get("/hello")
async def hello():
    return {"message": "Hello, World!"}