import httpx

from cfg import CITY, API_KEY


async def fetch_temperature() -> float | None:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        temperature = data.get("main", {}).get("temp")
        return temperature
