from datetime import datetime

from rich import print
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.usgs import USGSClient
from src.domain.earthquake import Earthquake
from src.repository.earthquake import EarthquakeRepository


class IngestService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = EarthquakeRepository(session)
        self.client = USGSClient()

    async def fetch_and_store_range(self, start_time: datetime, end_time: datetime) -> list[Earthquake]:
        print(f"[bold blue]IngestService:[/bold blue] Fetching from USGS between {start_time} and {end_time}...")

        try:
            feature_collection = await self.client.get_earthquakes(start_time, end_time)
            print(f"[bold blue]IngestService:[/bold blue] Found {feature_collection.metadata['count']} earthquakes.")

            saved_earthquakes = []

            for feature in feature_collection.features:
                earthquake_id = feature.id
                props = feature.properties
                geometry = feature.geometry.coordinates

                saved = await self.repo.save(props, earthquake_id, geometry)
                saved_earthquakes.append(saved)

            await self.session.commit()

            print(f"[bold green]IngestService:[/bold green] Successfully saved {len(saved_earthquakes)} records.")
            return saved_earthquakes

        except Exception as e:
            print(f"[bold red]IngestService Error:[/bold red] {e}")
            raise e
