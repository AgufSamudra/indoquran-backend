from fastapi import APIRouter

router = APIRouter(
    prefix="/hadist",
    tags=["hadist"]
)


@router.get("/")
async def hadist_main():
    return {"code": 200, "data": "API HADIST"}