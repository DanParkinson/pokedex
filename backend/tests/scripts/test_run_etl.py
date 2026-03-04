from pokedex.database.contracts import RESOURCE_CONTRACTS
from pokedex.scripts.run_etl import main


def test_run_etl_main_runs_full_pipeline(monkeypatch):
    # Arrange
    page1 = {
        "count": 4,
        "next": "http://next-page",
        "results": [{"url": "a"}, {"url": "b"}],
    }

    page2 = {
        "count": 4,
        "next": None,
        "results": [{"url": "c"}, {"url": "d"}],
    }

    monkeypatch.setattr(
        "pokedex.scripts.run_etl.api_entry_point",
        lambda resource, resource_id: page1,
    )

    monkeypatch.setattr(
        "pokedex.scripts.run_etl.fetch_json",
        lambda url: page2,
    )

    monkeypatch.setattr(
        "pokedex.scripts.run_etl.extract_data",
        lambda response: response["results"],
    )

    parse_calls = []

    def fake_parse(raw, contract):
        parse_calls.append((tuple(raw), contract["table"]))
        return [{"parsed": True} for _ in raw]

    monkeypatch.setattr(
        "pokedex.scripts.run_etl.parse_resource_batch",
        fake_parse,
    )

    load_calls = []

    def fake_load(rows, contract):
        load_calls.append((len(rows), contract["table"]))

    monkeypatch.setattr(
        "pokedex.scripts.run_etl.load_data_batch",
        fake_load,
    )

    # Act
    main("pokemon")

    # Assert
    # Number of pokemon-related contracts
    pokemon_contracts = [
        c for c in RESOURCE_CONTRACTS.values() if c["resource"] == "pokemon"
    ]
    num_contracts = len(pokemon_contracts)

    # parse_resource_batch called once per contract per page
    assert len(parse_calls) == num_contracts * 2

    # load_data_batch called once per contract per page
    assert len(load_calls) == num_contracts * 2

    # First page raw rows
    first_raw = ({"url": "a"}, {"url": "b"})
    # Second page raw rows
    second_raw = ({"url": "c"}, {"url": "d"})

    # Check first page calls
    for i in range(num_contracts):
        assert parse_calls[i][0] == first_raw

    # Check second page calls
    for i in range(num_contracts, num_contracts * 2):
        assert parse_calls[i][0] == second_raw

    # Check load row counts
    for count, table in load_calls:
        assert count == 2
