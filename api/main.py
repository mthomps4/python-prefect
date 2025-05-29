from fastapi import FastAPI
from routes.index import api_router

app = FastAPI(
    title="Prefect API",
    description="API for managing Prefect workflows",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api")