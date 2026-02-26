import pytest
import duckdb

from pokedex.scripts.init_db import main as init_db
from pokedex.database.connection import get_connection


# ===================
# Fixtures
# ===================
@pytest.fixture
def patched_db(tmp_path, monkeypatch):
    db_file = tmp_path / "test.duckdb"

    # Patch DB_PATH where get_connection() actually reads it
    monkeypatch.setattr("pokedex.database.connection.DB_PATH", db_file)

    # Helper to patch SCHEMA_SQL for each test
    def set_schema(schema_sql: str):
        monkeypatch.setattr("pokedex.scripts.init_db.SCHEMA_SQL", schema_sql)

    return db_file, set_schema


# ====================
# Utils
# ====================


def get_table_columns(db_path: str, table: str) -> set[str]:
    conn = duckdb.connect(db_path)
    rows = conn.execute(
        f"""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = '{table}'
        """
    ).fetchall()
    return {r[0] for r in rows}


def get_schema_tables(db_path: str) -> set[str]:
    conn = duckdb.connect(db_path)
    rows = conn.execute(
        """
        SELECT table_name,
        FROM information_schema.tables
        WHERE table_type = 'BASE TABLE'
        """
    ).fetchall()
    return {r[0] for r in rows}


# ===================
# Main
# ===================


def test_create_database_file_persistent(patched_db):
    # Arrange
    db_file, _ = patched_db

    # Act
    init_db()

    # Assert
    assert db_file.exists()


# ====================
# Connection
# ====================


def test_return_database_file_connection(patched_db):
    # Arrange
    db_file, _ = patched_db

    # Act
    conn = get_connection()

    # Assert
    assert conn is not None


def test_get_connection_creates_parent_directory(tmp_path, monkeypatch):
    nested = tmp_path / "foo" / "bar"
    db_file = nested / "test.duckdb"

    monkeypatch.setattr("pokedex.database.connection.DB_PATH", db_file)

    # precondition: directory does not exist
    assert not db_file.parent.exists()

    # Act
    conn = get_connection()

    # Assert
    assert db_file.parent.exists(), "parent directory should have been created"
    # connection is usable
    conn.execute("SELECT 1").fetchall()
    conn.close()


# ====================
# Validation of schema
# ====================


def test_validate_schema_columns(patched_db):
    # Arrange
    db_file, set_schema = patched_db

    TEST_SCHEMA = """
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY,
        test TEXT NOT NULL,
        test1 INTEGER
    );
    """

    # Act
    set_schema(TEST_SCHEMA)
    init_db()

    # Assert
    assert get_table_columns(db_file, "test") == {"id", "test", "test1"}


def test_validate_schema_tables(patched_db):
    # Arrange
    db_file, set_schema = patched_db

    TEST_SCHEMA = """
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY,
        test TEXT NOT NULL,
        test1 INTEGER
    );
    """
    # Act
    set_schema(TEST_SCHEMA)
    init_db()

    # Assert
    assert get_schema_tables(db_file) == {"test"}


def test_validate_apply_schema_idempotent(patched_db):
    db_file, set_schema = patched_db

    TEST_SCHEMA = """
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY,
        test TEXT NOT NULL,
        test1 INTEGER
    );
    """
    set_schema(TEST_SCHEMA)
    init_db()
    schema1 = get_table_columns(db_file, "test")

    init_db()
    schema2 = get_table_columns(db_file, "test")

    # Assert
    assert schema1 == schema2 == {"id", "test", "test1"}
