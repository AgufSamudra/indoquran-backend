# import all files in folder routes
from .quran import router as quran_router
from .hadist import router as hadist_router
from .search import router as search_router

from fastapi import APIRouter

router = APIRouter()
router.include_router(quran_router)
router.include_router(hadist_router)
router.include_router(search_router)