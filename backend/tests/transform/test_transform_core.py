import pytest

from pokedex.database.contracts import RESOURCE_CONTRACTS
from pokedex.transform.transform import parse_resource


# ===========
# Listings
# ===========
def test_parse_resource_pokemon_returns_expected():
    # Arrange
    response = {
        "id": 1,
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "weight": 69,
    }

    expected = {
        "id": 1,
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "weight": 69,
    }

    # Act
    result = parse_resource(response, RESOURCE_CONTRACTS["pokemon"])

    # Assert
    assert result == expected


def test_parse_resource_raises_on_missing_data():
    # missing "id"
    response = {
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "weight": 69,
    }

    with pytest.raises(KeyError):
        parse_resource(response, RESOURCE_CONTRACTS["pokemon"])
