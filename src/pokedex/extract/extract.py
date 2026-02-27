import requests
from pokedex.utils.logger import get_logger

logger = get_logger(__name__)

BASE_URL = "https://pokeapi.co/api/v2"


def build_resource_url(resource: str, resource_id: str = None) -> str:
    if resource_id is not None:
        return f"{BASE_URL}/{resource}/{resource_id}"
    return f"{BASE_URL}/{resource}"


def fetch_json(url: str) -> dict:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"HTTP request failed for {url}: {e}")
        raise
