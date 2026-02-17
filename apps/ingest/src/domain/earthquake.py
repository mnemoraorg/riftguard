from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime, timezone

class EarthquakeProperties(SQLModel):
    """
    Base model representing the properties of an earthquake.
    Used as the Pydantic schema for API responses and GeoJSON parsing.
    """
    mag: Optional[float] = None
    place: Optional[str] = None
    time: int = Field(index=True) # Index for time-range queries
    updated: int
    tz: Optional[int] = None
    url: Optional[str] = None
    detail: Optional[str] = None
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

    # Intensity & Impact
    felt: Optional[int] = None
    cdi: Optional[float] = None
    mmi: Optional[float] = None
    alert: Optional[str] = None

    @property
    def time_as_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.time / 1000.0, tz=timezone.utc)

class Earthquake(EarthquakeProperties, table=True):
    """
    Database model for the 'earthquakes' table.
    Inherits fields from EarthquakeProperties.
    """
    __tablename__ = "earthquakes"
    id: str = Field(primary_key=True)
