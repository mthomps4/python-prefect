from fastapi import APIRouter
from .examples import hello, example

api_router = APIRouter()

api_router.include_router(hello.router, prefix="/hello-world", tags=["hello-world"])
api_router.include_router(example.router, prefix="/example", tags=["example"])