from fastapi import APIRouter, BackgroundTasks
from typing import Dict
from pydantic import BaseModel
from utils.logger import get_logger

logger = get_logger(__name__)

class DataModel(BaseModel):
    name: str = "Hello World"

router = APIRouter()

#  Example of a long running task that runs in the background
async def long_running_task(data: Dict):
    # Simulate long running process
    import asyncio
    await asyncio.sleep(3)

    # Do something with the data
    logger.info(f"Completed processing data: {data}")
    return {"status": "completed", "data": data}

# Endpoint that triggers a background task and returns immediately
@router.post("/process")
async def process_in_background(background_tasks: BackgroundTasks, data: Dict):
    logger.info(f"Starting background task with data: {data}")
    # Add the task to background tasks
    background_tasks.add_task(long_running_task, data)

    return {
        "message": "Task started in background",
        "status": "processing"
    }
