import pytest
import requests

from pokedex.extract.http import fetch_json
from pokedex.extract.listings import extract_response_urls, parse_resource
from pokedex.extract.urls import build_resource_url


# ============
# Build URLS
# ============
def test_build_resource_url_builds_url_without_resource_id():
    # Arrange
    resource = "pokemon"
    expected_url = "https://pokeapi.co/api/v2/pokemon"

    # Act
    url = build_resource_url(resource)

    # Assert
    assert url == expected_url


def test_build_resource_url_builds_url_with_resource_id():
    resource = "pokemon"
    resource_id = "1"
    expected_url = "https://pokeapi.co/api/v2/pokemon/1"

    # Act
    url = build_resource_url(resource, resource_id)

    # Assert
    assert url == expected_url


# ============
# HTTP
# ============
def test_fetch_json_returns_json(requests_mock):
    # Arrange
    url = "https://example.com/test"
    expected = {"a": 1}
    requests_mock.get(url, json=expected)

    # Act
    result = fetch_json(url)

    # Assert
    assert result == expected


def test_fetch_json_raises_on_http_error(requests_mock):
    # Arrange
    url = "https://example.com/test"
    requests_mock.get(url, status_code=404)
    # Act and Assert
    with pytest.raises(requests.exceptions.HTTPError):
        fetch_json(url)


# ===========
# Listings
# ===========


def test_extract_repsonse_urls_returns_urlS():
    # Arrange
    response = {
        "count": 1281,
        "next": "https://pokeapi.co/api/v2/pokemon?offset=20&limit=20",
        "previous": "null",
        "results": [
            {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
            {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"},
        ],
    }

    expected = [
        "https://pokeapi.co/api/v2/pokemon/1/",
        "https://pokeapi.co/api/v2/pokemon/2/",
    ]

    # Act
    urls = extract_response_urls(response)

    # Assert
    assert urls == expected


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
