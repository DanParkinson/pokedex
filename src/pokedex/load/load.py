from pokedex.database.connection import get_connection
from pokedex.database.contracts import RESOURCE_CONTRACTS
from pokedex.utils.logger import get_logger

logger = get_logger(__name__)


def load_data_batch(data: list[dict], resource: str | None = None) -> None:
    for row in data:
        load_data(row, resource)


def load_data(row: dict, resource: str | None = None) -> None:
    contract = RESOURCE_CONTRACTS[resource]
    required = contract["output_fields"]

    # Validate
    for key in required:
        if key not in row:
            logger.error(f"Missing required field '{key}'")
            raise KeyError

    # Build SQL
    table = resource
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
    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()
