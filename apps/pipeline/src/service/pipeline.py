from datetime import datetime

from rich import print
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.usgs import USGSClient
from src.domain.earthquake import Earthquake
from src.repository.earthquake import EarthquakeRepository


async def fetch_and_store_earthquakes(
    session: AsyncSession,
    start_time: datetime,
    end_time: datetime,
    usgs_client: USGSClient = None,
) -> list[Earthquake]:
    if usgs_client is None:
        usgs_client = USGSClient()

    repo = EarthquakeRepository(session)

    print(f"[bold blue]Pipeline:[/bold blue] Fetching from USGS between {start_time} and {end_time}...")

    try:
        feature_collection = await usgs_client.get_earthquakes(start_time, end_time)
        print(f"[bold blue]Pipeline:[/bold blue] Found {feature_collection.metadata['count']} earthquakes.")

        saved_earthquakes = []

        for feature in feature_collection.features:
            earthquake_id = feature.id
            props = feature.properties

            saved = await repo.save(props, earthquake_id)
            saved_earthquakes.append(saved)

        print(f"[bold green]Pipeline:[/bold green] Successfully saved/updated {len(saved_earthquakes)} records.")
        return saved_earthquakes

    except Exception as e:
        print(f"[bold red]Pipeline Error:[/bold red] {e}")
        raise e
