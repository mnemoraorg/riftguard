from fastapi import FastAPI

from src.routes.v1 import router as v1_router

app = FastAPI(
    title="Riftguard Pipeline Service",
    description="Processes earthquake data from USGS and serves it to the processing pipeline.",
    version="1.0.0",
)

app.include_router(v1_router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
