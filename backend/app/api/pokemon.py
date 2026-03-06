from fastapi import APIRouter

from .calls import fetch_pokemon_card_basic
from .schemas import PokemonCardBasic

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/pokemon", response_model=list[PokemonCardBasic])
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
