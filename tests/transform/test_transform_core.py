import pytest

from pokedex.transform.transform import parse_resource


# ===========
# Listings
# ===========
def test_parse_resource_returns_expected():
    response = {
        "id": 1,
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "weight": 69,
        "dont_want_key": "dont_want_value",
    }

    expected = {
        "id": 1,
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "weight": 69,
    }

    data = parse_resource(response)

    assert data == expected


def test_parse_reource_raises_on_missing_data():
    """Missing id"""
    response = {
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "weight": 69,
        "dont_want_key": "dont_want_value",
    }

    with pytest.raises(KeyError):
        parse_resource(response)
