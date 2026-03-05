SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    base_experience INTEGER,
    height INTEGER,
    weight INTEGER,
);

CREATE TABLE IF NOT EXISTS pokemon_stats (
    id INTEGER PRIMARY KEY REFERENCES pokemon(id),
    hp INTEGER NOT NULL,
    attack INTEGER NOT NULL,
    defense INTEGER NOT NULL,
    special_attack INTEGER NOT NULL,
    special_defense INTEGER NOT NULL,
    speed INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS pokemon_sprites (
    id INTEGER PRIMARY KEY REFERENCES pokemon(id),
    official_artwork_front TEXT,
    home_front TEXT,
    front_default TEXT,
    back_default TEXT,
    front_shiny TEXT,
    back_shiny TEXT
);

CREATE TABLE IF NOT EXISTS pokemon_abilities (
    id INTEGER PRIMARY KEY REFERENCES pokemon(id),
    ability_1 TEXT,
    ability_1_hidden BOOLEAN,
    ability_1_slot INTEGER,
    ability_2 TEXT,
    ability_2_hidden BOOLEAN,
    ability_2_slot INTEGER
);

CREATE TABLE IF NOT EXISTS pokemon_types (
    id INTEGER PRIMARY KEY REFERENCES pokemon(id),
    type_1 TEXT,
    type_1_slot INTEGER,
    type_2 TEXT,
    type_2_slot INTEGER
);

CREATE TABLE IF NOT EXISTS pokemon_weaknesses (
    id INTEGER PRIMARY KEY REFERENCES pokemon(id),
    normal REAL,
    fire REAL,
    water REAL,
    electric REAL,
    grass REAL,
    ice REAL,
    fighting REAL,
    poison REAL,
    ground REAL,
    flying REAL,
    psychic REAL,
    bug REAL,
    rock REAL,
    ghost REAL,
    dragon REAL,
    dark REAL,
    steel REAL,
    fairy REAL
);

"""
