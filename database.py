from databases import Database
from sqlalchemy import (
    MetaData,
    create_engine,
    Table,
    Column,
    Integer,
    String,
    DateTime,
    Float,
)

from cfg import DATABASE_URL

metadata = MetaData()

weather_data = Table(
    "weather_data",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("city", String),
    Column("date_time", DateTime),
    Column("temperature", Float),
)
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

database = Database(DATABASE_URL)
