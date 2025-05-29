from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def healthcheck():
    return {
        "message": "This is a health check endpoint",
        "version": "1.0.0"
    }