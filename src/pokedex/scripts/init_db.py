import duckdb
from pathlib import Path

from pokedex.database.schema import SCHEMA_SQL
from pokedex.utils.logger import get_logger

DB_PATH = Path("data/pokedex.duckdb")

logger = get_logger(__name__)

def init_db(schema: str):
    conn = duckdb.connect(str(DB_PATH))
    conn.execute(schema)
    return conn
    

if __name__ == "__main__":
    init_db(SCHEMA_SQL)