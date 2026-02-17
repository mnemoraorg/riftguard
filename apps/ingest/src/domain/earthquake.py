from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional

class EarthquakeProperties(BaseModel):
    mag: Optional[float] = None
    place: Optional[str] = None
    time: int
    updated: int
    tz: Optional[int] = None
    url: Optional[str] = None
    detail: Optional[str] = None
    felt: Optional[int] = None
    cdi: Optional[float] = None
    mmi: Optional[float] = None
    alert: Optional[str] = None
    status: Optional[str] = None
    tsunami: Optional[int] = None
    sig: Optional[int] = None
    net: Optional[str] = None
    code: Optional[str] = None
    ids: Optional[str] = None
    sources: Optional[str] = None
    types: Optional[str] = None
    nst: Optional[int] = None
    dmin: Optional[float] = None
    rms: Optional[float] = None
    gap: Optional[float] = None
    magType: Optional[str] = None
    type: str
    title: str

    @property
    def time_as_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.time / 1000.0, tz=timezone.utc)
