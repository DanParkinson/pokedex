from pokedex.extract.http import fetch_json
from pokedex.extract.listings import extract_response_urls, parse_resource
from pokedex.extract.urls import build_resource_url
from pokedex.utils.logger import get_logger

logger = get_logger(__name__)


def extract_pokemon(resource: str, resource_id: str = None) -> list[dict]:
    logger.info(f"Beginning Extraction of {resource} data...")

    url = build_resource_url(resource, resource_id)
    response = fetch_json(url)
    urls = extract_response_urls(response)

    data = []

    for url in urls:
        response = fetch_json(url)
        data.append(parse_resource(response))

    return data
