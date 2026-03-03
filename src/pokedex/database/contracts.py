RESOURCE_CONTRACTS = {
    "pokemon": {
        # raw API fields
        "required": [
            "id",
            "name",
            "base_experience",
            "height",
            "weight",
            "types",
            "stats",
            "sprites",
        ],
        # parsed output fields
        "output_fields": [
            "id",
            "name",
            "base_experience",
            "height",
            "weight",
            "sprite",
            "type_1",
            "type_2",
            "hp",
            "attack",
            "defense",
            "special_attack",
            "special_defense",
            "speed",
        ],
        # transform logic
        "desired": lambda r: {
            "id": r["id"],
            "name": r["name"],
            "base_experience": r["base_experience"],
            "height": r["height"],
            "weight": r["weight"],
            # modern sprite (official artwork)
            "sprite": r["sprites"]["other"]["official-artwork"]["front_default"],
            # types
            "type_1": sorted(r["types"], key=lambda t: t["slot"])[0]["type"]["name"],
            "type_2": (
                sorted(r["types"], key=lambda t: t["slot"])[1]["type"]["name"]
                if len(r["types"]) > 1
                else None
            ),
            # stats
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
}
