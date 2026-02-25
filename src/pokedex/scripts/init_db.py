import duckdb
from pathlib import Path

from pokedex.utils.logger import get_logger

DB_PATH = Path("data/pokedex.duckdb")

logger = get_logger(__name__)

def init_db():
    duckdb.connect(str(DB_PATH))
    

if __name__ == "__main__":
    init_db()