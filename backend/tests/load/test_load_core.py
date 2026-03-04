from unittest.mock import MagicMock, patch

import duckdb
import pytest

from pokedex.database.contracts import RESOURCE_CONTRACTS
from pokedex.load.load import load_data


def test_load_data_closes_connection():
    mock_conn = MagicMock()

    # must include ALL required output_fields for pokemon
    dummy_row = {
        "id": 1,
        "name": "test",
        "base_experience": 10,
        "height": 1,
        "weight": 1,
    }

    with patch("pokedex.load.load.get_connection", return_value=mock_conn):
        load_data(dummy_row, RESOURCE_CONTRACTS["pokemon"])

    mock_conn.close.assert_called_once()


def test_load_data_inserts_row_succesfully(tmp_path):
    db_path = tmp_path / "test.duckdb"
    conn = duckdb.connect(str(db_path))

    conn.execute("""
        CREATE TABLE pokemon (
            id INTEGER PRIMARY KEY,
            name TEXT,
            base_experience INTEGER,
            height INTEGER,
            weight INTEGER,
        );
    """)
    conn.close()

    row = {
        "id": 25,
        "name": "pikachu",
        "base_experience": 112,
        "height": 4,
        "weight": 60,
    }

    with patch(
        "pokedex.load.load.get_connection", return_value=duckdb.connect(str(db_path))
    ):
        load_data(row, RESOURCE_CONTRACTS["pokemon"])

    conn = duckdb.connect(str(db_path))
    result = conn.execute("""
        SELECT id, name, base_experience, height, weight,
        FROM pokemon
    """).fetchall()

    assert result == [(25, "pikachu", 112, 4, 60)]


def test_load_data_raises_on_missing_data():
    """Missing id"""
    response = {
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "weight": 69,
        "dont_want_key": "dont_want_value",
    }

    with pytest.raises(KeyError):
        load_data(response, RESOURCE_CONTRACTS["pokemon"])
