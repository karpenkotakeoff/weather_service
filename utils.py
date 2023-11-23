from datetime import datetime, date

from fastapi import HTTPException

from cfg import X_TOKEN, CITY
from models import TemperatureResponseModel, HourlyTempsModel


def validate_token(x_token: str) -> None:
    if x_token != X_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid X-Token header")


def handle_temperatures_result(
        from_date: date, result: list[tuple[int, str, datetime, float]]
) -> TemperatureResponseModel:
    hourly_temps = []
    for record in result:
        _, _, date_time, temperature = record
        hourly_temps.append(HourlyTempsModel(time=date_time.time(), temperature=temperature))
    return TemperatureResponseModel(city=CITY, date=from_date, hourly_temps=hourly_temps)
