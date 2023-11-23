import asyncio
from datetime import datetime

from cfg import CITY
from database import weather_data, database
from openweather import fetch_temperature

TEMP_FETCH_PERIOD = 3600  # seconds


async def add_temperature():
    while True:
        temperature = await fetch_temperature()
        if temperature is not None:
            query = weather_data.insert().values(date_time=datetime.now(), city=CITY, temperature=temperature)
            await database.execute(query)
        await asyncio.sleep(TEMP_FETCH_PERIOD)
