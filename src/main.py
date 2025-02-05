from fastapi import FastAPI
from src.v1.routes import router as v1_router

# initialize fastapi as a app
app = FastAPI()
app.include_router(v1_router, prefix="/api/v1")
