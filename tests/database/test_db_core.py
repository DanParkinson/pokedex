import duckdb
from pokedex.scripts.init_db import init_db


def test_create_database_file_persistent(tmp_path, monkeypatch):
    # Arrange
    monkeypatch.setattr(
        "pokedex.database.connection.DB_PATH", tmp_path / "pokedex.duckdb"
    )

    # Act
    init_db()

    # Assert
    assert (tmp_path / "pokedex.duckdb").exists()


def test_validate_table_schema(tmp_path, monkeypatch):
    # Arrange
    TEST_SCHEMA = """
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY,
        test TEXT NOT NULL,
        test1 INTEGER
    );
    """

    EXPECTED_ROWS = {"id", "test", "test1"}

    monkeypatch.setattr("pokedex.database.connection.DB_PATH", tmp_path / "test.duckdb")
    monkeypatch.setattr("pokedex.scripts.init_db.SCHEMA_SQL", TEST_SCHEMA)

    # Act
    conn = init_db()

    # Assert
    conn = duckdb.connect(tmp_path / "test.duckdb")
    rows = conn.execute(
        """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = 'test'
    """
    ).fetchall()

    actual = {r[0] for r in rows}
    assert actual == EXPECTED_ROWS
