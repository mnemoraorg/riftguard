from datetime import datetime

from pydantic import BaseModel


class IngestRangeRequest(BaseModel):
    start_time: datetime
    end_time: datetime
