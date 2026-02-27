import requests

from pokedex.utils.logger import get_logger

logger = get_logger(__name__)


def fetch_json(url: str) -> dict:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"HTTP request failed for {url}: {e}")
        raise
