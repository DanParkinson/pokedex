def apply_schema(conn, schema: str) -> None:
    conn.execute(schema)
