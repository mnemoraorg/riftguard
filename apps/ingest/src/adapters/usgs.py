import httpx
from datetime import datetime

from src.domain.feature import FeatureCollection

from src.config.env import settings

USGS_BASE_URL = settings.USGS_BASE_URL

class USGSClient:
    def __init__(self, base_url: str = USGS_BASE_URL):
        self.base_url = base_url

    async def get_earthquakes(self, start_time: datetime, end_time: datetime) -> FeatureCollection:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/query",
                params={
                    "format": "geojson",
                    "starttime": start_time.isoformat(),
                    "endtime": end_time.isoformat(),
                },
                timeout=30.0
            )
            response.raise_for_status()
            return FeatureCollection(**response.json())
