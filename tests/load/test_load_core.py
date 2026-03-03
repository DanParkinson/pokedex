from unittest.mock import MagicMock, patch

import duckdb
import pytest

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
        "sprite": "url",
        "type_1": "grass",
        "type_2": None,
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "special_attack": 65,
        "special_defense": 65,
        "speed": 45,
    }

    with patch("pokedex.load.load.get_connection", return_value=mock_conn):
        load_data(dummy_row, resource="pokemon")

    mock_conn.close.assert_called_once()


def test_load_data_inserts_expected_row(tmp_path):
    db_path = tmp_path / "test.duckdb"
    conn = duckdb.connect(str(db_path))

    conn.execute("""
        CREATE TABLE pokemon (
            id INTEGER PRIMARY KEY,
            name TEXT,
            base_experience INTEGER,
            height INTEGER,
            weight INTEGER,
            sprite TEXT,
            type_1 TEXT,
            type_2 TEXT,
            hp INTEGER,
            attack INTEGER,
            defense INTEGER,
            special_attack INTEGER,
            special_defense INTEGER,
            speed INTEGER
        );
    """)
    conn.close()

    row = {
        "id": 25,
        "name": "pikachu",
        "base_experience": 112,
        "height": 4,
        "weight": 60,
        "sprite": "url",
        "type_1": "electric",
        "type_2": None,
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special_attack": 50,
        "special_defense": 50,
        "speed": 90,
    }

    with patch(
        "pokedex.load.load.get_connection", return_value=duckdb.connect(str(db_path))
    ):
        load_data(row, resource="pokemon")

    conn = duckdb.connect(str(db_path))
    result = conn.execute("""
        SELECT id, name, base_experience, height, weight,
               sprite, type_1, type_2, hp, attack, defense,
               special_attack, special_defense, speed
        FROM pokemon
    """).fetchall()

    assert result == [
        (25, "pikachu", 112, 4, 60, "url", "electric", None, 35, 55, 40, 50, 50, 90)
    ]


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
        load_data(response, resource="pokemon")
