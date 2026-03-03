from pokedex.database.contracts import RESOURCE_CONTRACTS
from pokedex.utils.logger import get_logger

logger = get_logger(__name__)


def parse_resource_batch(responses: list[dict], resource: str) -> list[dict]:
    return [parse_resource(response, resource) for response in responses]


def parse_resource(response: str, resource: str) -> dict:
    contract = RESOURCE_CONTRACTS[resource]
    required = contract["required"]
    desired = contract["desired"]

    for key in required:
        if key not in response:
            logger.error(f"Missing required field: {key}")
            raise KeyError

    return desired(response)
