from fastapi import APIRouter
from prefect.client import get_client
from pydantic import BaseModel

router = APIRouter()

class HelloRequest(BaseModel):
    name: str

@router.post("/")
async def run_job(request: HelloRequest):
    async with get_client() as client:
        await client.create_flow_run_from_deployment(
            flow_id="hello-world",
            parameters={"name": request.name},
        )
    return {"status": "Job triggered"}