from fastapi import APIRouter

router = APIRouter(
    prefix="/quran",
    tags=["quran"]
)


@router.get("/surat")
async def surat():
    pass


@router.get("/surat_detail")
async def detail_surat():
    pass


@router.get("/tafsir")
async def tafsir():
    pass