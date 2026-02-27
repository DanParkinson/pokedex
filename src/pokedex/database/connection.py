from pathlib import Path

import duckdb

from pokedex.errors import DatabaseConnectionError
from pokedex.utils.logger import get_logger

logger = get_logger(__name__)

DB_PATH = Path("data/pokedex.duckdb")


def get_connection() -> duckdb.DuckDBPyConnection:
    try:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        return duckdb.connect(str(DB_PATH))
    except duckdb.Error as e:
        logger.error(f"Connection failed: {e}")
        raise DatabaseConnectionError(str(e))
