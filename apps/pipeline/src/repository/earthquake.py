from datetime import UTC, datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.domain.earthquake import Earthquake, EarthquakeProperties


class EarthquakeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, properties: EarthquakeProperties, id: str, geometry: list[float]) -> Earthquake:
        data = properties.model_dump()
        data["id"] = id

        # GeoJSON coordinates are [longitude, latitude, depth]
        if len(geometry) >= 3:
            data["longitude"] = geometry[0]
            data["latitude"] = geometry[1]
            data["depth"] = geometry[2]
        elif len(geometry) == 2:
            data["longitude"] = geometry[0]
            data["latitude"] = geometry[1]
            data["depth"] = 0.0

        # Data Cleaning & Transformation

        # 1. Convert timestamp (ms) to datetime
        if isinstance(data.get("time"), (int, float)):
            data["time"] = datetime.fromtimestamp(data["time"] / 1000.0, tz=UTC)

        if isinstance(data.get("updated"), (int, float)):
            data["updated"] = datetime.fromtimestamp(data["updated"] / 1000.0, tz=UTC)

        # 2. Strip commas from specific fields
        for field in ["ids", "sources", "types"]:
            if isinstance(data.get(field), str):
                data[field] = data[field].strip(",")

        earthquake = Earthquake.model_validate(data)

        saved = await self.session.merge(earthquake)
        return saved

    async def get_recent(self, limit: int = 10) -> list[Earthquake]:
        stmt = select(Earthquake).order_by(Earthquake.time.desc()).limit(limit)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())
