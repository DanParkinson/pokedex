from pydantic import BaseModel


class PokemonCardBasic(BaseModel):
    id: int
    name: str
    sprite: str | None = None
