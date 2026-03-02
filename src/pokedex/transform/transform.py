from pokedex.database.contracts import REQUIRED_FIELDS_POKEMON
from pokedex.utils.logger import get_logger

logger = get_logger(__name__)


def parse_resource_batch(responses: list[dict]) -> list[dict]:
    data = []
    logger.info("Transforming data...")
    for response in responses:
        data.append(parse_resource(response))
    logger.info("Data transformed successfully")
    return data


def parse_resource(response: str) -> dict:
    required = REQUIRED_FIELDS_POKEMON

    for key in required:
        if key not in response:
            logger.error(f"Missing required field: {key}")
            raise KeyError
    data = {
        "id": response["id"],
        "name": response["name"],
        "base_experience": response["base_experience"],
        "weight": response["weight"],
        "height": response["height"],
    }
    return data
