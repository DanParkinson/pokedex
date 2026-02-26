from pokedex.utils.logger import get_logger

from pokedex.database.schema import SCHEMA_SQL
from pokedex.database.connection import get_connection

logger = get_logger(__name__)

def init_db(schema: str):
    conn = get_connection()
    conn.execute(schema)
    return conn
    

if __name__ == "__main__":
    init_db(SCHEMA_SQL)