import requests

from pokedex.utils.logger import get_logger

logger = get_logger(__name__)

BASE_URL = "https://pokeapi.co/api/v2"


def extract_pokemon(resource: str, resource_id: str = None) -> list[dict]:
    logger.info(f"Beginning Extraction of {resource} data...")

    url = build_resource_url(resource, resource_id)
    response = fetch_json(url)
    urls = extract_response_urls(response)

    data = []

    for url in urls:
        response = fetch_json(url)
        data.append(response)

    logger.info(f"Finished Extraction of {resource} data.")

    return data


# ==========
# Helpers
# ==========


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


def extract_response_urls(response: dict) -> list:
    return [item["url"] for item in response["results"]]
