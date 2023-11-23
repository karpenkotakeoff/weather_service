from datetime import date, time

from pydantic import BaseModel

from cfg import CITY


class HourlyTempsModel(BaseModel):
    time: time
    temperature: float


class TemperatureResponseModel(BaseModel):
    city: str = CITY
    date: date
    hourly_temps: list[HourlyTempsModel]
