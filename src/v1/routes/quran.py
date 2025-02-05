from fastapi import APIRouter

router = APIRouter(
    prefix="/quran",
    tags=["quran"]
)


@router.get("/")
async def quran_main():
    return {"code": 200, "data": "API QURAN"}