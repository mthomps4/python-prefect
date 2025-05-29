from fastapi import APIRouter
from .feature import health, hello, background, testLog

api_router = APIRouter()

# Test Logger Import
api_router.include_router(testLog.router, prefix="/test-log", tags=["test-log"])
# Normal Fast API Route
api_router.include_router(health.router, prefix="/healthcheck", tags=["healthcheck"])
# Fast API Route that triggers a Prefect Flow
api_router.include_router(hello.router, prefix="/hello-world", tags=["hello-world"])
# Fast API Route that runs a background task (FastAPI Worker)
api_router.include_router(background.router, prefix="/background", tags=["background"])
