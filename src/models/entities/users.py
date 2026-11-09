from sqlalchemy import Column, Integer, String, Table

from src.models.settings.metadata import metadata

Users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_name", String, nullable=True),
    Column("age", Integer),
    Column("uf", String),
)
