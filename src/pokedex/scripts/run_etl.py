from pokedex.extract.extract import extract_pokemon

BASE_URL = "https://pokeapi.co/api/v2"


def main():
    pokemon_data = extract_pokemon("pokemon")
    print(pokemon_data[1:6])


if __name__ == "__main__":
    main()
