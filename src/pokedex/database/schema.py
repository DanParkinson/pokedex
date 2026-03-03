EXPECTED_TABLES = {
    "pokemon",
}

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    base_experience INTEGER,
    height INTEGER,
    weight INTEGER,
    sprite TEXT,
    type_1 TEXT NOT NULL,
    type_2 TEXT,
    hp INTEGER NOT NULL,
    attack INTEGER NOT NULL,
    defense INTEGER NOT NULL,
    special_attack INTEGER NOT NULL,
    special_defense INTEGER NOT NULL,
    speed INTEGER NOT NULL
);
"""
