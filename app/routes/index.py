from fastapi import APIRouter
from .feature import hello, example, background

api_router = APIRouter()

api_router.include_router(hello.router, prefix="/hello-world", tags=["hello-world"])
api_router.include_router(example.router, prefix="/example", tags=["example"])
api_router.include_router(background.router, prefix="/background", tags=["fastAPI"])