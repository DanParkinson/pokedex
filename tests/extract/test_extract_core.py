import requests
import pytest

from pokedex.extract.extract import build_resource_url, fetch_json


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
