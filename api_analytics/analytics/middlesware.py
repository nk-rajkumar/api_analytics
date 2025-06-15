from starlette.requests import Request
from sqlalchemy.orm import Session
from datetime import datetime
from user_agents import parse

from api_analytics.analytics.models import analytics_api
from api_analytics.db import get_db


def extract_request_data(request: Request):
    ip_address = request.client.host
    raw_user_data = request.headers.get("user-agent", "unknown")
    ua = parse(raw_user_data)
    os = ua.os.family
    user_agent = ua.browser.family
    return ip_address, user_agent, os


async def update_analytics(request: Request):

    db_generator = get_db()
    db: Session = next(db_generator)

    if request.method == "POST":
        request_id = "product/create-item"
    elif request.method == "PUT":
        request_id = "product/update-item"
    elif request.method == "DELETE":
        request_id = "product/delete-item"
    else:
        request_id = "product/get-item"

    request_type = request.method
    request_time = datetime.now()
    ip_address, user_agent, os = extract_request_data(request)
    pay_load = None
    content_type = request.headers.get("content-type", "unknown")

    if request.method in ["POST", "PUT"]:
        try:
            body_data = await request.body()
            pay_load = body_data.decode()
        except:
            pay_load = None
        content_type = request.headers.get("content-type", "unknown")

    hit = analytics_api(
        request_id=request_id,
        request_type=request_type,
        request_time=request_time,
        ip_address=ip_address,
        user_agent=user_agent,
        os=os,
        pay_load=pay_load,
        content_type=content_type,
    )
    db.add(hit)
    db.commit()
    db_generator.close()
