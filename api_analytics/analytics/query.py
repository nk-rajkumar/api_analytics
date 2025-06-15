from sqlalchemy.orm import Session
from api_analytics.analytics.models import analytics_api
from typing import Optional


def get_filters(
    db: Session,
    request_id: Optional[str] = None,
    request_type: Optional[str] = None,
    ip_address: Optional[str] = None,
    os: Optional[str] = None,
    user_agent: Optional[str] = None,
):

    filters = {}

    if request_id:
        filters[analytics_api.request_id.name] = request_id
    if request_type:
        filters[analytics_api.request_type.name] = request_type.upper()
    if ip_address:
        filters[analytics_api.ip_address.name] = ip_address
    if os:
        filters[analytics_api.os.name] = os
    if user_agent:
        filters[analytics_api.user_agent.name] = user_agent

    query = db.query(analytics_api)
    query = query.filter_by(**filters)

    return query.all()
