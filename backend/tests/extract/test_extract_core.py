import pytest
import requests

from pokedex.extract.extract import (
    api_entry_point,
    build_resource_url,
    extract_data,
    extract_response_urls,
    fetch_json,
)


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
def test_extract_repsonse_urls_returns_urls():
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


def test_api_entry_point_returns_json(requests_mock):
    # Arrange
    resource = "pokemon"
    resource_id = "1"
    expected = {"name": "bulbasaur"}
    url = f"https://pokeapi.co/api/v2/{resource}/{resource_id}"
    requests_mock.get(url, json=expected)

    # Act
    result = api_entry_point(resource, resource_id)

    # Assert
    assert result == expected


# ============
# Extraction
# ============
def test_extract_data_returns_list_of_dicts(monkeypatch):
    # Arrange
    response = {
        "results": [
            {"url": "https://example.com/1"},
            {"url": "https://example.com/2"},
        ]
    }

    expected = [
        {"id": 1, "value": "a"},
        {"id": 2, "value": "b"},
    ]

    # Patch fetch_json to return each dict in order
    monkeypatch.setattr(
        "pokedex.extract.extract.fetch_json", lambda url: expected.pop(0)
    )

    # Act
    result = extract_data(response)

    # Assert
    assert result == [
        {"id": 1, "value": "a"},
        {"id": 2, "value": "b"},
    ]
