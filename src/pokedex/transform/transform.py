from pokedex.utils.logger import get_logger

logger = get_logger(__name__)


def parse_resource(response: str) -> dict:
    required = ["id", "name", "base_experience", "weight", "height"]

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
