from pokedex.database.connection import get_connection


def test_return_database_file_connection(tmp_path, monkeypatch):
    # Arrange
    monkeypatch.setattr("pokedex.database.connection.DB_PATH", tmp_path / "test.duckdb")

    # Act
    conn = get_connection()

    # Assert
    assert conn is not None
