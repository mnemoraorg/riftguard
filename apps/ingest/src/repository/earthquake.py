from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.repository.models import EarthquakeModel
from src.domain.earthquake import EarthquakeProperties
from typing import List

class EarthquakeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, earthquake: EarthquakeProperties) -> EarthquakeModel:
        """
        Save or update an earthquake record.
        Uses `merge` to handle upserts based on the primary key (id).
        """
        # Convert Pydantic model to dict, excluding None to let DB defaults work if any
        data = earthquake.model_dump(exclude={"type"})
        
        model = EarthquakeModel(**data)
        model.type_ = earthquake.type # Manually map 'type' field
        
        # Merge handles upsert (insert or update)
        saved = await self.session.merge(model)
        return saved
    
    async def save_all(self, earthquakes: List[EarthquakeProperties]):
        """Batch save earthquakes."""
        for eq in earthquakes:
            await self.save(eq)
        await self.session.flush()

    async def get_recent(self, limit: int = 10) -> List[EarthquakeModel]:
        """Get the most recent earthquakes."""
        stmt = select(EarthquakeModel).order_by(EarthquakeModel.time.desc()).limit(limit)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())
