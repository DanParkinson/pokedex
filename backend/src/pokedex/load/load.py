from pokedex.database.connection import get_connection
from pokedex.utils.logger import get_logger

logger = get_logger(__name__)


def load_data_batch(data: list[dict], contract: dict) -> None:
    for row in data:
        load_data(row, contract)


def load_data(row: dict, contract: dict) -> None:
    required = contract["output_fields"]

    # Validate
    for key in required:
        if key not in row:
            logger.error(f"Missing required field '{key}'")
            raise KeyError

    # Build SQL
    table = contract["table"]
    columns = list(row.keys())
    placeholders = ", ".join(["?"] * len(columns))
    colnames = ", ".join(columns)

    sql = f"""
        INSERT INTO {table} ({colnames})
        VALUES ({placeholders})
        ON CONFLICT(id) DO NOTHING
    """

    conn = get_connection()

    try:
        conn.execute("BEGIN")
        conn.execute(sql, [row[c] for c in columns])
        conn.execute("COMMIT")
        print(f"Inserted into {table}: {row}")

    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()
