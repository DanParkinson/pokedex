TYPE_CHART = {
    "normal": {"rock": 0.5, "ghost": 0.0, "steel": 0.5},
    "fire": {
        "fire": 0.5,
        "water": 0.5,
        "grass": 2,
        "ice": 2,
        "bug": 2,
        "rock": 0.5,
        "dragon": 0.5,
        "steel": 2,
    },
    "water": {
        "fire": 2,
        "water": 0.5,
        "grass": 0.5,
        "ground": 2,
        "rock": 2,
        "dragon": 0.5,
    },
    "electric": {
        "water": 2,
        "electric": 0.5,
        "grass": 0.5,
        "ground": 0,
        "flying": 2,
        "dragon": 0.5,
    },
    "grass": {
        "fire": 0.5,
        "water": 2,
        "grass": 0.5,
        "poison": 0.5,
        "ground": 2,
        "flying": 0.5,
        "bug": 0.5,
        "rock": 2,
        "dragon": 0.5,
        "steel": 0.5,
    },
    "ice": {
        "fire": 0.5,
        "water": 0.5,
        "grass": 2,
        "ice": 0.5,
        "ground": 2,
        "flying": 2,
        "dragon": 2,
        "steel": 0.5,
    },
    "fighting": {
        "normal": 2,
        "ice": 2,
        "rock": 2,
        "dark": 2,
        "steel": 2,
        "poison": 0.5,
        "flying": 0.5,
        "psychic": 0.5,
        "bug": 0.5,
        "ghost": 0,
    },
    "poison": {
        "grass": 2,
        "fairy": 2,
        "poison": 0.5,
        "ground": 0.5,
        "rock": 0.5,
        "ghost": 0.5,
        "steel": 0,
    },
    "ground": {
        "fire": 2,
        "electric": 2,
        "poison": 2,
        "rock": 2,
        "steel": 2,
        "grass": 0.5,
        "bug": 0.5,
        "flying": 0,
    },
    "flying": {
        "grass": 2,
        "fighting": 2,
        "bug": 2,
        "electric": 0.5,
        "rock": 0.5,
        "steel": 0.5,
    },
    "psychic": {"fighting": 2, "poison": 2, "psychic": 0.5, "steel": 0.5, "dark": 0},
    "bug": {
        "grass": 2,
        "psychic": 2,
        "dark": 2,
        "fire": 0.5,
        "fighting": 0.5,
        "poison": 0.5,
        "flying": 0.5,
        "ghost": 0.5,
        "steel": 0.5,
        "fairy": 0.5,
    },
    "rock": {
        "fire": 2,
        "ice": 2,
        "flying": 2,
        "bug": 2,
        "fighting": 0.5,
        "ground": 0.5,
        "steel": 0.5,
    },
    "ghost": {"psychic": 2, "ghost": 2, "dark": 0.5, "normal": 0},
    "dragon": {"dragon": 2, "steel": 0.5, "fairy": 0},
    "dark": {"psychic": 2, "ghost": 2, "fighting": 0.5, "dark": 0.5, "fairy": 0.5},
    "steel": {
        "ice": 2,
        "rock": 2,
        "fairy": 2,
        "fire": 0.5,
        "water": 0.5,
        "electric": 0.5,
        "steel": 0.5,
    },
    "fairy": {
        "fighting": 2,
        "dragon": 2,
        "dark": 2,
        "fire": 0.5,
        "poison": 0.5,
        "steel": 0.5,
    },
}


RESOURCE_CONTRACTS = {
    "pokemon": {
        "resource": "pokemon",
        "resource_id": None,
        "table": "pokemon",
        # raw API fields
        "required": [
            "id",
            "name",
            "base_experience",
            "height",
            "weight",
        ],
        # parsed output fields
        "output_fields": [
            "id",
            "name",
            "base_experience",
            "height",
            "weight",
        ],
        # transform logic
        "desired": lambda r: {
            "id": r["id"],
            "name": r["name"],
            "base_experience": r["base_experience"],
            "height": r["height"],
            "weight": r["weight"],
        },
    },
    "pokemon_stats": {
        "resource": "pokemon",
        "resource_id": None,
        "table": "pokemon_stats",
        "required": ["id", "stats"],
        "output_fields": [
            "id",
            "hp",
            "attack",
            "defense",
            "special_attack",
            "special_defense",
            "speed",
        ],
        "desired": lambda r: {
            "id": r["id"],
            "hp": next(s["base_stat"] for s in r["stats"] if s["stat"]["name"] == "hp"),
            "attack": next(
                s["base_stat"] for s in r["stats"] if s["stat"]["name"] == "attack"
            ),
            "defense": next(
                s["base_stat"] for s in r["stats"] if s["stat"]["name"] == "defense"
            ),
            "special_attack": next(
                s["base_stat"]
                for s in r["stats"]
                if s["stat"]["name"] == "special-attack"
            ),
            "special_defense": next(
                s["base_stat"]
                for s in r["stats"]
                if s["stat"]["name"] == "special-defense"
            ),
            "speed": next(
                s["base_stat"] for s in r["stats"] if s["stat"]["name"] == "speed"
            ),
        },
    },
    "pokemon_sprites": {
        "resource": "pokemon",
        "resource_id": None,
        "table": "pokemon_sprites",
        "required": ["id", "sprites"],
        "output_fields": [
            "id",
            "official_artwork_front",
            "home_front",
            "front_default",
            "back_default",
            "front_shiny",
            "back_shiny",
        ],
        "desired": lambda r: {
            "id": r["id"],
            "official_artwork_front": (
                r["sprites"]["other"]["official-artwork"]["front_default"]
                if r["sprites"]["other"]["official-artwork"]["front_default"]
                else None
            ),
            "home_front": (
                r["sprites"]["other"]["home"]["front_default"]
                if r["sprites"]["other"]["home"]["front_default"]
                else None
            ),
            "front_default": r["sprites"]["front_default"],
            "back_default": r["sprites"]["back_default"],
            "front_shiny": r["sprites"]["front_shiny"],
            "back_shiny": r["sprites"]["back_shiny"],
        },
    },
    "pokemon_abilities": {
        "resource": "pokemon",
        "resource_id": None,
        "table": "pokemon_abilities",
        "required": ["id", "abilities"],
        "output_fields": [
            "id",
            "ability_1",
            "ability_1_hidden",
            "ability_1_slot",
            "ability_2",
            "ability_2_hidden",
            "ability_2_slot",
        ],
        "desired": lambda r: {
            "id": r["id"],
            "ability_1": r["abilities"][0]["ability"]["name"]
            if len(r["abilities"]) > 0
            else None,
            "ability_1_hidden": r["abilities"][0]["is_hidden"]
            if len(r["abilities"]) > 0
            else None,
            "ability_1_slot": r["abilities"][0]["slot"]
            if len(r["abilities"]) > 0
            else None,
            "ability_2": r["abilities"][1]["ability"]["name"]
            if len(r["abilities"]) > 1
            else None,
            "ability_2_hidden": r["abilities"][1]["is_hidden"]
            if len(r["abilities"]) > 1
            else None,
            "ability_2_slot": r["abilities"][1]["slot"]
            if len(r["abilities"]) > 1
            else None,
        },
    },
    "pokemon_types": {
        "resource": "pokemon",
        "resource_id": None,
        "table": "pokemon_types",
        "required": ["id", "types"],
        "output_fields": ["id", "type_1", "type_1_slot", "type_2", "type_2_slot"],
        "desired": lambda r: {
            "id": r["id"],
            "type_1": (
                sorted(r["types"], key=lambda t: t["slot"])[0]["type"]["name"]
                if len(r["types"]) > 0
                else None
            ),
            "type_1_slot": (
                sorted(r["types"], key=lambda t: t["slot"])[0]["slot"]
                if len(r["types"]) > 0
                else None
            ),
            "type_2": (
                sorted(r["types"], key=lambda t: t["slot"])[1]["type"]["name"]
                if len(r["types"]) > 1
                else None
            ),
            "type_2_slot": (
                sorted(r["types"], key=lambda t: t["slot"])[1]["slot"]
                if len(r["types"]) > 1
                else None
            ),
        },
    },
    "pokemon_weaknesses": {
        "resource": "pokemon",
        "resource_id": None,
        "table": "pokemon_weaknesses",
        "required": ["id", "types"],
        "output_fields": [
            "id",
            "normal",
            "fire",
            "water",
            "electric",
            "grass",
            "ice",
            "fighting",
            "poison",
            "ground",
            "flying",
            "psychic",
            "bug",
            "rock",
            "ghost",
            "dragon",
            "dark",
            "steel",
            "fairy",
        ],
        "desired": lambda r: (
            lambda t1, t2: {
                "id": r["id"],
                **{
                    atk: (
                        TYPE_CHART.get(atk, {}).get(t1, 1.0)
                        * (TYPE_CHART.get(atk, {}).get(t2, 1.0) if t2 else 1.0)
                    )
                    for atk in [
                        "normal",
                        "fire",
                        "water",
                        "electric",
                        "grass",
                        "ice",
                        "fighting",
                        "poison",
                        "ground",
                        "flying",
                        "psychic",
                        "bug",
                        "rock",
                        "ghost",
                        "dragon",
                        "dark",
                        "steel",
                        "fairy",
                    ]
                },
            }
        )(
            sorted(r["types"], key=lambda t: t["slot"])[0]["type"]["name"],
            sorted(r["types"], key=lambda t: t["slot"])[1]["type"]["name"]
            if len(r["types"]) > 1
            else None,
        ),
    },
}
