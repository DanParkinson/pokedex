import duckdb
from pathlib import Path

from pokedex.utils.logger import get_logger

DB_PATH = Path("data/pokedex.duckdb")

logger = get_logger(__name__)

def init_db():
    conn = duckdb.connect(str(DB_PATH))
    return conn
    

if __name__ == "__main__":
    init_db()