from fastapi import APIRouter

from api.endpoints import generate

api_router = APIRouter()

api_router.include_router(
    generate.generate_router,
    prefix="/generate",
    tags=["generate"]
)
