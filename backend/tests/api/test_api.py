from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_pokemon_card_basic():
    response = client.get("/pokemon")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

    # If the DB is populated, we expect at least one Pokémon
    assert len(data) > 0

    first = data[0]
    assert "id" in first
    assert "name" in first
    assert "sprite" in first

    assert isinstance(first["id"], int)
    assert isinstance(first["name"], str)
    assert first["sprite"] is None or isinstance(first["sprite"], str)
