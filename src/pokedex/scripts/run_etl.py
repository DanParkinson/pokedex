from pokedex.extract.extract import api_entry_point, extract_data
from pokedex.extract.http import fetch_json
from pokedex.load.load import load_data_batch
from pokedex.transform.transform import parse_resource_batch
from pokedex.utils.logger import get_logger

logger = get_logger(__name__)


def main(resource: str, resource_id: str = None) -> None:
    response = api_entry_point(resource, resource_id)

    total = response["count"]
    next_url = response["next"]
    parsed = 0

    while True:
        batch = response["results"]

        raw = extract_data(response)
        data = parse_resource_batch(raw)
        load_data_batch(data)

        parsed = parsed + len(batch)
        logger.info(f"Loaded {parsed}/{total} {resource}")

        if not next_url:
            break

        response = fetch_json(next_url)
        next_url = response["next"]


if __name__ == "__main__":
    main("pokemon")
