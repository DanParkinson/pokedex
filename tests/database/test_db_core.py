from pokedex.scripts.init_db import init_db

TEST_SCHEMA = """
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY,
        test TEXT NOT NULL,
        test1 INTEGER,
    );
    """

def test_create_database_file_persistent(tmp_path, monkeypatch):
    # Arrange
    monkeypatch.setattr("pokedex.scripts.init_db.DB_PATH", tmp_path / "pokedex.duckdb")

    # Act
    init_db(TEST_SCHEMA)

    # Assert
    assert(tmp_path / "pokedex.duckdb").exists()

def test_return_database_file_connection(tmp_path, monkeypatch):
    # Arrange
    monkeypatch.setattr("pokedex.scripts.init_db.DB_PATH", tmp_path / "pokedex.duckdb")

    # Act
    conn = init_db(TEST_SCHEMA)

    # Assert
    assert conn is not None

def test_validate_table_schema(tmp_path, monkeypatch):
    # Arrange
    monkeypatch.setattr("pokedex.scripts.init_db.DB_PATH", tmp_path / "pokedex.duckdb")

    EXPECTED_ROWS = {
        "id",
        "test",
        "test1"
    }

    # Act
    conn = init_db(TEST_SCHEMA)

    # Assert

    rows = conn.execute(
        """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = 'test' 
    """).fetchall()

    actual = {r[0] for r in rows}
    assert actual == EXPECTED_ROWS