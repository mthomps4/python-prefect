from fastapi import APIRouter
from utils.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)

@router.get("/")
async def test_logging():
    """Test endpoint that demonstrates logger usage"""
    logger.info("This is a test info log message")
    logger.warning("This is a test warning message")
    logger.error("This is a test error message")

    return {"message": "Logging test completed successfully"}
