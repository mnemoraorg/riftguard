from typing import Any

from pydantic import BaseModel

from src.domain.earthquake import EarthquakeProperties


class Geometry(BaseModel):
    type: str
    coordinates: list[float]


class Feature(BaseModel):
    type: str
    properties: EarthquakeProperties
    geometry: Geometry
    id: str


class FeatureCollection(BaseModel):
    type: str
    metadata: dict[str, Any]
    features: list[Feature]
