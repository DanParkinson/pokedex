from pokedex.scripts.init_db import init_db

def test_create_database_file_persistent(tmp_path, monkeypatch):
    # Arrange
    monkeypatch.setattr("pokedex.scripts.init_db.DB_PATH", tmp_path / "pokedex.duckdb")

    # Act
    init_db()

    # Assert
    assert(tmp_path / "pokedex.duckdb").exists()

def test_return_database_file_connection(tmp_path, monkeypatch):
    # Arrange
    monkeypatch.setattr("pokedex.scripts.init_db.DB_PATH", tmp_path / "pokedex.duckdb")

    # Act
    conn = init_db()

    # Assert
    assert conn is not None

