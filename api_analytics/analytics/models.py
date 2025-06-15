from sqlalchemy import String, Text, Integer, Column, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class analytics_api(Base):
    __tablename__ = "apihits"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(String, index=True)
    request_type = Column(String)
    request_time = Column(DateTime, default=datetime.now)
    pay_load = Column(Text, nullable=True)
    content_type = Column(String, nullable=True)
    ip_address = Column(String)
    os = Column(String)
    user_agent = Column(String)
