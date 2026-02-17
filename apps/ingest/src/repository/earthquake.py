from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.earthquake import Earthquake, EarthquakeProperties
from typing import List

class EarthquakeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, properties: EarthquakeProperties, id: str) -> Earthquake:
        """
        Save or update an earthquake record.
        """
        # Create Earthqake table instance from properties
        # We need to inject the ID which is part of Feature, not Properties
        data = properties.model_dump()
        data["id"] = id
        
        earthquake = Earthquake.model_validate(data)
        
        # Merge handles upsert
        saved = await self.session.merge(earthquake)
        return saved
    
    async def get_recent(self, limit: int = 10) -> List[Earthquake]:
        """Get the most recent earthquakes."""
        stmt = select(Earthquake).order_by(Earthquake.time.desc()).limit(limit)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())
