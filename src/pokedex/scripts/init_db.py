from pokedex.database.connection import get_connection
from pokedex.database.migrate import apply_schema
from pokedex.database.schema import SCHEMA_SQL
from pokedex.errors import DatabaseError
from pokedex.utils.logger import get_logger

logger = get_logger(__name__)


def main():
    logger.info("Initializing Database...")
    try:
        with get_connection() as conn:
            apply_schema(conn, SCHEMA_SQL)
    except DatabaseError as e:
        logger.error(f"Database initialization failed: {e}")
        raise
    logger.info("Database Initialized.")


if __name__ == "__main__":
    main()
