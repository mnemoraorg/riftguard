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


async def delete_all_view(db: AsyncSession = Depends(get_db)):
    service = IngestService(db)
    try:
        deleted_count = await service.delete_all()
        return {
            "status": "success",
            "deleted_count": deleted_count,
            "message": f"Successfully deleted {deleted_count} earthquakes.",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
