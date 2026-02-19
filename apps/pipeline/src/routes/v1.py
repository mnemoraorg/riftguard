from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.db import get_db
from src.dto.ingest import IngestRangeRequest
from src.views.ingest import ingest_range_view

router = APIRouter()


@router.post("/ingest/range")
async def ingest_range(payload: IngestRangeRequest, db: AsyncSession = Depends(get_db)):
    return await ingest_range_view(payload, db)
