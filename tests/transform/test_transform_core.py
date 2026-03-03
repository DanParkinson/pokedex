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
        "types": [
            {"slot": 1, "type": {"name": "grass"}},
            {"slot": 2, "type": {"name": "poison"}},
        ],
        "stats": [
            {"stat": {"name": "hp"}, "base_stat": 45},
            {"stat": {"name": "attack"}, "base_stat": 49},
            {"stat": {"name": "defense"}, "base_stat": 49},
            {"stat": {"name": "special-attack"}, "base_stat": 65},
            {"stat": {"name": "special-defense"}, "base_stat": 65},
            {"stat": {"name": "speed"}, "base_stat": 45},
        ],
        "sprites": {
            "other": {
                "official-artwork": {"front_default": "http://example.com/sprite.png"}
            }
        },
        "dont_want_key": "ignore_me",
    }

    expected = {
        "id": 1,
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "weight": 69,
        "sprite": "http://example.com/sprite.png",
        "type_1": "grass",
        "type_2": "poison",
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "special_attack": 65,
        "special_defense": 65,
        "speed": 45,
    }

    data = parse_resource(response, "pokemon")

    assert data == expected


def test_parse_resource_raises_on_missing_data():
    # missing "id"
    response = {
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "weight": 69,
        "types": [],
        "stats": [],
        "sprites": {},
    }

    with pytest.raises(KeyError):
        parse_resource(response, "pokemon")
