import asyncio
from contextlib import asynccontextmanager
from datetime import date

import uvicorn
from fastapi import FastAPI, Header, Query
from fastapi.responses import RedirectResponse
from sqlalchemy import func

from cfg import APP_HOST, APP_PORT
from database import weather_data, database
from models import TemperatureResponseModel
from tasks import add_temperature
from utils import validate_token, handle_temperatures_result


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(add_temperature())
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse(url="/docs")


@app.get("/temperatures")
async def get_temperatures(
        from_date: date = Query(description="Date in YYYY-MM-DD format"), x_token: str = Header(None)
) -> TemperatureResponseModel:
    validate_token(x_token)
    query = weather_data.select().where(func.date(weather_data.c.date_time) == from_date)
    result = await database.fetch_all(query)
    return handle_temperatures_result(from_date, result)


if __name__ == "__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
