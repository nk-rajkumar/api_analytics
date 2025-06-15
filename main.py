from fastapi import FastAPI, Request
from api_analytics.product.services import product
from api_analytics.analytics.services import analytics
from api_analytics.analytics.middlesware import update_analytics
from api_analytics.db import engine
from api_analytics.analytics.models import Base


@product.middleware("http")
async def analytics_middlesware(request: Request, call_next):
    await update_analytics(request)
    res = await call_next(request)

    return res


Base.metadata.create_all(bind=engine)


app = FastAPI()
app.mount("/product", product)
app.mount("/analytics", analytics)
