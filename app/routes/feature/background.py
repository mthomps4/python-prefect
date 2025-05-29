from fastapi import APIRouter, BackgroundTasks
from typing import Dict

router = APIRouter()

async def long_running_task(data: Dict):
    """
    Example of a long running task that runs in the background
    """
    # Simulate long running process
    import asyncio
    await asyncio.sleep(3)
    # Do something with the data
    print(f"Completed processing data: {data}")
    return {"status": "completed"}

@router.post("/process")
async def process_in_background(background_tasks: BackgroundTasks, data: Dict):
    """
    Endpoint that triggers a background task and returns immediately
    """
    # Add the task to background tasks
    background_tasks.add_task(long_running_task, data)

    return {
        "message": "Task started in background",
        "status": "processing"
    }
