from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule
from hello_world import hello_world

# Create a deployment for the hello-world flow
deployment = Deployment.build_from_flow(
    flow=hello_world,
    name="hello-world",
    version="1",
    work_queue_name="default",
)

if __name__ == "__main__":
    deployment.apply()