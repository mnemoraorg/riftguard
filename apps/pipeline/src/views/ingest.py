from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.db import get_db
from src.dto.ingest import IngestRangeRequest
from src.service.ingest import IngestService

router = APIRouter()


async def ingest_range_view(payload: IngestRangeRequest, db: AsyncSession = Depends(get_db)):
    service = IngestService(db)
    try:
        results = await service.fetch_and_store_range(payload.start_time, payload.end_time)
        return {"status": "success", "count": len(results), "message": f"Ingested {len(results)} earthquakes."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
