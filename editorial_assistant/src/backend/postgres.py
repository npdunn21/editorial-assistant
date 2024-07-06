import os
from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy import Table, Column, Integer, String, MetaData, UUID, VARCHAR


_ENGINE = None
_CLIENT_TABLE: Optional[Table] = None


def initialize_database():
    """
    TK
    :return:
    """
    metadata_obj = MetaData()
    _CLIENT_TABLE = Table(
        "client",
        metadata_obj,
        Column("id", UUID, primary_key=True, nullable=False),
        Column("name", VARCHAR, nullable=False),
        Column("description", VARCHAR),
        Column("nickname", VARCHAR, nullable=False),
    )


def get_client_table() -> Table:
    """
    Get and return the Client table
    """
    if _CLIENT_TABLE is None:
        initialize_database()
        return _CLIENT_TABLE
    return _CLIENT_TABLE


def get_async_engine() -> AsyncEngine:
    """
    Gets asynchronous sqlalchemy engine for postgresql
    """
    return create_async_engine(os.getenv("DATABASE_PATH"), echo=True)
