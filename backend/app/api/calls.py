from .connection import get_connection_api


def fetch_pokemon_card_basic(limit: int = None):
    conn = get_connection_api()
    try:
        rows = conn.execute(
            """
            SELECT
                p.id,
                p.name,
                s.home_front AS sprite
            FROM
                pokemon AS p
            LEFT JOIN
                pokemon_sprites s ON p.id = s.id
            LIMIT
                ?
            """,
            [limit],
        ).fetchall()
        return rows
    finally:
        conn.close()
