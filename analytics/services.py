from fastapi import FastAPI, Depends
from api_analytics.db import get_db
from api_analytics.analytics.schemas import APIHitBase
from api_analytics.analytics.middlesware import Session
from api_analytics.analytics.query import get_filters
from typing import List, Optional

analytics = FastAPI(prefix="/analytics")


@analytics.get("/list", response_model=List[APIHitBase])
def list_api_hits(
    request_id: Optional[str] = None,
    request_type: Optional[str] = None,
    ip_address: Optional[str] = None,
    os: Optional[str] = None,
    user_agent: Optional[str] = None,
    db: Session = Depends(get_db),
):
    return get_filters(
        db,
        request_id=request_id,
        request_type=request_type,
        ip_address=ip_address,
        os=os,
        user_agent=user_agent,
    )
