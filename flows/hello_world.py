from prefect import flow, task
from typing import Optional

@task
def say_hello(name: str) -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"

@task
def log_greeting(greeting: str) -> None:
    """Log the greeting."""
    print(greeting)

@flow(name="hello-world")
def hello_world(name: Optional[str] = "World"):
    """A simple hello world flow."""
    greeting = say_hello(name)
    log_greeting(greeting)
    return greeting

if __name__ == "__main__":
    hello_world()