from fastapi import APIRouter, HTTPException
from prefect.client import get_client
from pydantic import BaseModel
from prefect.states import Scheduled

try:
    from prefect.client.schemas.responses import StateCreate
    StateCreate.model_rebuild()
except ImportError:
    pass

router = APIRouter()

class HelloRequest(BaseModel):
    name: str | None = "World"

@router.post("/")
async def run_job(request: HelloRequest):
    try:
        async with get_client() as client:
            # Get the deployment by name
            deployment = await client.read_deployment_by_name("hello-world/hello-world")
            if not deployment:
                raise HTTPException(
                    status_code=404,
                    detail="Deployment 'hello-world/hello-world' not ¬found"
                )

            flow_run = await client.create_flow_run_from_deployment(
                deployment_id=deployment.id,
                parameters={"name": request.name},
            )
            return {
                "status": "Job triggered",
                "flow_run_id": flow_run.id
            }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to trigger flow: {str(e)}"
        )