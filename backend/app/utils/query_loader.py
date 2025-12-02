# backend/app/utils/query_loader.py
import re
from pathlib import Path

def load_named_queries(file_path: str):
    """
    Parse a queries.sql file and return {query_name: query_sql}
    """
    text = Path(file_path).read_text(encoding="utf-8")

    # Split on markers like "-- name: query_name"
    blocks = re.split(r"--\s*name:\s*", text)
    queries = {}

    for block in blocks[1:]:
        lines = block.strip().splitlines()
        name = lines[0].strip()
        sql = "\n".join(lines[1:]).strip().rstrip(";")
        queries[name] = sql

    return queries
