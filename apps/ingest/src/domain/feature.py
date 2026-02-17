from pydantic import BaseModel
from typing import List, Optional, Any, Dict

from src.domain.earthquake import EarthquakeProperties

class Geometry(BaseModel):
    type: str
    coordinates: List[float]

class Feature(BaseModel):
    type: str 
    properties: EarthquakeProperties
    geometry: Geometry
    id: str

class FeatureCollection(BaseModel):
    type: str 
    metadata: Dict[str, Any]
    features: List[Feature]
