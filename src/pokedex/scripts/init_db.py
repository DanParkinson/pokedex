from pokedex.utils.logger import get_logger

from pokedex.database.schema import SCHEMA_SQL
from pokedex.database.connection import get_connection
from pokedex.database.migrate import apply_schema

logger = get_logger(__name__)


def init_db():
    with get_connection() as conn:
        apply_schema(conn, SCHEMA_SQL)


if __name__ == "__main__":
    init_db()
