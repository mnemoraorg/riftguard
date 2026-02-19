from datetime import UTC, datetime

from sqlalchemy import BigInteger
from sqlmodel import Field, SQLModel


class EarthquakeProperties(SQLModel):
    mag: float | None = None
    place: str | None = None
    time: int = Field(sa_type=BigInteger, index=True)
    updated: int = Field(sa_type=BigInteger)
    tz: int | None = None
    url: str | None = None
    detail: str | None = None
    status: str | None = None
    tsunami: int | None = None
    sig: int | None = None
    net: str | None = None
    code: str | None = None
    ids: str | None = None
    sources: str | None = None
    types: str | None = None
    nst: int | None = None
    dmin: float | None = None
    rms: float | None = None
    gap: float | None = None
    magType: str | None = None
    type: str
    title: str

    felt: int | None = None
    cdi: float | None = None
    mmi: float | None = None
    alert: str | None = None

    @property
    def time_as_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.time / 1000.0, tz=UTC)


class Earthquake(EarthquakeProperties, table=True):
    __tablename__ = "earthquakes"
    id: str = Field(primary_key=True)

    # Overriding fields to be datetime in DB
    time: datetime = Field(index=True)
    updated: datetime

    latitude: float = Field(default=0.0)
    longitude: float = Field(default=0.0)
    depth: float = Field(default=0.0)
