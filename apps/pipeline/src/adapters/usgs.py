from datetime import datetime

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from src.config.env import settings
from src.domain.feature import FeatureCollection

USGS_BASE_URL = settings.USGS_BASE_URL


class USGSClient:
    def __init__(self, base_url: str = USGS_BASE_URL):
        self.base_url = base_url

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type((httpx.ConnectError, httpx.TimeoutException, httpx.ReadTimeout)),
    )
    async def get_earthquakes(self, start_time: datetime, end_time: datetime) -> FeatureCollection:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/query",
                    params={
                        "format": "geojson",
                        "starttime": start_time.isoformat(),
                        "endtime": end_time.isoformat(),
                    },
                    timeout=30.0,
                )
                response.raise_for_status()
                return FeatureCollection(**response.json())
            except httpx.HTTPStatusError as e:
                # Don't retry inside the client if it's a 4xx, but maybe for 5xx
                if e.response.status_code >= 500:
                    raise e
                raise e  # Re-raise for now
