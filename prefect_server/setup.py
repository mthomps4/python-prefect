import sys
from prefect.client.orchestration import get_client
from prefect.server.schemas.actions import WorkPoolCreate
import time

async def ensure_default_work_pool():
    try:
        async with get_client() as client:
            existing_pools = await client.read_work_pools()
            if not any(pool.name == "default" for pool in existing_pools):
                await client.create_work_pool(
                    work_pool=WorkPoolCreate(
                        name="default",
                        type="process",
                    )
                )
                print("Created default work pool.")
            else:
                print("Default work pool already exists.")
        return True
    except Exception as e:
        print(f"Error ensuring default work pool: {str(e)}")
        return False


def deploy_flows():
    try:
        # Import the flow using the correct path
        from flows.hello_world import hello_world

        # Serve (deploy) these flows when the app is running
        # will upsert the deployment in the database
        hello_world.serve(
            tags=["hello-world", "default"],
            name="hello-world",
            version="1",
        )

        print("Successfully deployed hello-world flow")
        return True
    except Exception as e:
        print(f"Error deploying flows: {str(e)}")
        return False

if __name__ == "__main__":
    # Try to deploy with retries
    max_retries = 5
    retry_delay = 5  # seconds

    # Create an async event loop to run the async function
    import asyncio
    has_default_work_pool = asyncio.run(ensure_default_work_pool())
    if not has_default_work_pool:
        print("Failed to create default work pool")
        sys.exit(1)

    for attempt in range(max_retries):
        if deploy_flows():
            sys.exit(0)
        print(f"Retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries})")
        time.sleep(retry_delay)

    print("Failed to deploy flows after maximum retries")
    sys.exit(1)