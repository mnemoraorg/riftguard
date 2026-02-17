from sqlalchemy import Column, Integer, String, Float, BigInteger, Text
from src.adapters.db import Base

class EarthquakeModel(Base):
    __tablename__ = "earthquakes"

    id = Column(String, primary_key=True, index=True) 
    
    # Core Features
    mag = Column(Float, nullable=True)
    place = Column(String, nullable=True)
    time = Column(BigInteger, index=True)
    updated = Column(BigInteger)
    tz = Column(Integer, nullable=True)
    url = Column(String, nullable=True)
    detail = Column(String, nullable=True)
    status = Column(String, nullable=True)
    tsunami = Column(Integer, nullable=True)
    sig = Column(Integer, nullable=True)
    net = Column(String, nullable=True)
    code = Column(String, nullable=True)
    ids = Column(String, nullable=True)
    sources = Column(String, nullable=True)
    types = Column(String, nullable=True)
    nst = Column(Integer, nullable=True)
    dmin = Column(Float, nullable=True)
    rms = Column(Float, nullable=True)
    gap = Column(Float, nullable=True)
    magType = Column(String, nullable=True)
    type_ = Column("type", String, nullable=True) 
    title = Column(String, nullable=True)

    felt = Column(Integer, nullable=True)
    cdi = Column(Float, nullable=True)
    mmi = Column(Float, nullable=True)
    alert = Column(String, nullable=True)
