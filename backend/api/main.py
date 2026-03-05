from fastapi import FastAPI

from api.calls import fetch_pokemon_card_basic
from api.schemas import PokemonCardBasic

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/pokemon", response_model=list[PokemonCardBasic])
def get_pokemon_card_basic():
    rows = fetch_pokemon_card_basic()
    return [
        PokemonCardBasic(
            id=row[0],
            name=row[1],
            sprite=row[2],
        )
        for row in rows
    ]
