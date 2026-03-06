from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parents[3]
DB_PATH = ROOT / "backend" / "data" / "pokedex.duckdb"


def get_connection_api():
    # Read only connection to DuckDB file
    return duckdb.connect(str(DB_PATH), read_only=True)
