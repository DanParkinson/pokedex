BASE_URL = "https://pokeapi.co/api/v2"


def build_resource_url(resource: str, resource_id: str = None) -> str:
    if resource_id is not None:
        return f"{BASE_URL}/{resource}/{resource_id}"
    return f"{BASE_URL}/{resource}"
