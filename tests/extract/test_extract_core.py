from pokedex.extract.extract import build_resource_url


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
