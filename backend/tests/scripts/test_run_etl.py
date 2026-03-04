from unittest.mock import patch

from pokedex.scripts.run_etl import main


def test_run_etl_paginates_with_next_page(caplog):
    first_page = {
        "count": 4,
        "next": "http://api/page2",
        "results": [{"name": "a"}, {"name": "b"}],
    }

    second_page = {
        "count": 4,
        "next": None,
        "results": [{"name": "c"}, {"name": "d"}],
    }

    with (
        patch("pokedex.scripts.run_etl.api_entry_point", return_value=first_page),
        patch("pokedex.scripts.run_etl.fetch_json", side_effect=[second_page]),
        patch(
            "pokedex.scripts.run_etl.extract_data", side_effect=lambda r: r["results"]
        ),
        patch(
            "pokedex.scripts.run_etl.parse_resource_batch", side_effect=lambda r, *_: r
        ),
        patch("pokedex.scripts.run_etl.load_data_batch") as load_mock,
    ):
        main("pokemon")

    assert load_mock.call_count == 2


def test_run_etl_stops_when_next_page_none():
    single_page = {
        "count": 2,
        "next": None,
        "results": [{"name": "a"}, {"name": "b"}],
    }

    with (
        patch("pokedex.scripts.run_etl.api_entry_point", return_value=single_page),
        patch("pokedex.scripts.run_etl.fetch_json") as fetch_mock,
        patch(
            "pokedex.scripts.run_etl.extract_data", side_effect=lambda r: r["results"]
        ),
        patch(
            "pokedex.scripts.run_etl.parse_resource_batch", side_effect=lambda r, *_: r
        ),
        patch("pokedex.scripts.run_etl.load_data_batch") as load_mock,
    ):
        main("pokemon")

    assert load_mock.call_count == 1
    fetch_mock.assert_not_called()
