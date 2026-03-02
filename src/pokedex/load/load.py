from pokedex.database.connection import get_connection
from pokedex.database.contracts import REQUIRED_FIELDS_POKEMON
from pokedex.utils.logger import get_logger

logger = get_logger(__name__)


def load_data_batch(data: list[dict]) -> None:
    for row in data:
        load_data(row)


def load_data(row: dict) -> None:
    required = REQUIRED_FIELDS_POKEMON

    for key in required:
        if key not in row:
            logger.error(f"Missing required field '{key}'")
            raise KeyError

    conn = get_connection()

    try:
        conn.execute("BEGIN")
        conn.execute(
            """
            INSERT INTO pokemon (id, name, base_experience, height, weight)
            VALUES(?, ?, ?, ?, ?)
            ON CONFLICT(id) DO NOTHING
            """,
            [
                row["id"],
                row["name"],
                row["base_experience"],
                row["height"],
                row["weight"],
            ],
        )
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()
