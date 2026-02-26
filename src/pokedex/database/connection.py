import duckdb
from pathlib import Path

from pokedex.utils.logger import get_logger

logger = get_logger(__name__)

DB_PATH = Path("data/pokedex.duckdb")

def get_connection() -> duckdb.DuckDBPyConnection:
    return duckdb.connect(str(DB_PATH))