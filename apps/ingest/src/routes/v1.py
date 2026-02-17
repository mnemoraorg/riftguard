from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.adapters.db import get_db
from src.repository.earthquake import EarthquakeRepository
from src.domain.earthquake import EarthquakeProperties

router = APIRouter()

@router.get("/earthquakes", response_model=List[dict]) 
async def get_recent_earthquakes(limit: int = 10,  db: AsyncSession = Depends(get_db)):
    repo = EarthquakeRepository(db)
    results = await repo.get_recent(limit=limit)
    return results
