EXPECTED_TABLES = {
    "pokemon",
}


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    base_experience INTEGER,
    weight INTEGER,
    height INTEGER
);
"""
