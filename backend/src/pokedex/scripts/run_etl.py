from pokedex.database.contracts import RESOURCE_CONTRACTS
from pokedex.extract.extract import api_entry_point, extract_data, fetch_json
from pokedex.load.load import load_data_batch
from pokedex.transform.transform import parse_resource_batch
from pokedex.utils.logger import get_logger

logger = get_logger(__name__)


def main(resource: str = "pokemon", resource_id=None):

    # limit for dev
    limit = 0

    contracts = [
        contract
        for contract in RESOURCE_CONTRACTS.values()
        if contract["resource"] == resource
    ]

    response = api_entry_point(resource, resource_id)
    total = response["count"]
    next_url = response["next"]
    parsed = 0

    while True:
        batch = response["results"]

        raw = extract_data(response)

        for contract in contracts:
            table = contract["table"]
            rows = parse_resource_batch(raw, contract)
            load_data_batch(rows, contract)
            logger.info(f"Loaded {len(rows)} rows into {table}")

        limit += 1
        parsed += len(batch)
        logger.info(f"Processed {parsed}/{total} Pokémon")

        if not next_url or limit == 2:
            break

        response = fetch_json(next_url)
        next_url = response["next"]


if __name__ == "__main__":
    main("pokemon")
