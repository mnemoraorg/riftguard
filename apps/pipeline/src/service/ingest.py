from datetime import datetime

from rich import print
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.usgs import USGSClient
from src.domain.earthquake import Earthquake
from src.repository.ingest import IngestRepository


class IngestService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = IngestRepository(session)
        self.client = USGSClient()

    async def fetch_and_store_range(self, start_time: datetime, end_time: datetime) -> list[Earthquake]:
        print(f"IngestService: Fetching from USGS between {start_time} and {end_time}...")

        try:
            feature_collection = await self.client.get_earthquakes(start_time, end_time)
            print(f"IngestService: Found {feature_collection.metadata['count']} earthquakes.")

            saved_earthquakes = []

            for feature in feature_collection.features:
                earthquake_id = feature.id
                props = feature.properties
                geometry = feature.geometry.coordinates

                saved = await self.repo.save(props, earthquake_id, geometry)
                saved_earthquakes.append(saved)

            await self.session.commit()

            print(f"IngestService: Successfully saved {len(saved_earthquakes)} records.")
            return saved_earthquakes

        except Exception as e:
            print(f"IngestService Error: {e}")
            raise e

    async def delete_all(self) -> int:
        print("IngestService: Deleting all ingested earthquakes...")
        try:
            deleted_count = await self.repo.delete_all()
            await self.session.commit()
            print(f"IngestService: Successfully deleted {deleted_count} records.")
            return deleted_count
        except Exception as e:
            await self.session.rollback()
            print(f"IngestService Error during deletion: {e}")
            raise e
