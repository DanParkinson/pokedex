from pokedex.extract.extract import extract_pokemon
from pokedex.load.load import load_data_batch
from pokedex.transform.transform import parse_resource_batch

BASE_URL = "https://pokeapi.co/api/v2"


def main():
    raw_pokemon_data = extract_pokemon("pokemon")
    pokemon_data = parse_resource_batch(raw_pokemon_data)
    load_data_batch(pokemon_data)


if __name__ == "__main__":
    main()
