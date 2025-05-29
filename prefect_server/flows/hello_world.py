from prefect import flow, task
from typing import Optional
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@task
def say_hello(name: str) -> str:
    """Say hello to someone."""
    print(f"Saying hello to {name}")
    logger.info(f"Saying hello to {name}")
    return f"Hello, {name}!"

@task
def log_greeting(greeting: str) -> None:
    """Log the greeting."""
    logger.info(f"Logging greeting: {greeting}")
    print(f"Logging greeting: {greeting}")

@flow(name="hello-world")
def hello_world(name: Optional[str] = "World"):
    """A simple hello world flow."""
    greeting = say_hello(name)
    log_greeting(greeting)
    return greeting

if __name__ == "__main__":
    hello_world()