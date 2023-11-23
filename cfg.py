import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY")
X_TOKEN = os.getenv("X_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
APP_HOST = os.getenv("APP_HOST")
APP_PORT = int(os.getenv("APP_PORT"))
