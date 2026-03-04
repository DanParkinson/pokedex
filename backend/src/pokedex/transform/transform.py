from pokedex.utils.logger import get_logger

logger = get_logger(__name__)


def parse_resource_batch(responses: list[dict], contract: dict) -> list[dict]:
    return [parse_resource(response, contract) for response in responses]


def parse_resource(response: str, contract: dict) -> dict:
    required = contract["required"]
    desired = contract["desired"]

    for key in required:
        if key not in response:
            logger.error(f"Missing required field: {key}")
            raise KeyError

    return desired(response)
