from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class APIHitBase(BaseModel):
    id: int
    request_id: str
    request_type: str
    request_time: datetime
    pay_load: Optional[str] = None
    content_type: Optional[str] = None
    ip_address: str
    os: str
    user_agent: str

    class Config:
        orm_mode = True
