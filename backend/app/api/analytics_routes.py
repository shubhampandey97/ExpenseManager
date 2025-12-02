# backend/app/api/analytics_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.utils.query_loader import load_named_queries
from pathlib import Path

router = APIRouter(prefix="/analytics", tags=["Analytics"])

QUERIES_FILE = Path(__file__).resolve().parent.parent / "sql" / "queries.sql"
QUERIES = load_named_queries(str(QUERIES_FILE))


@router.get("/list", response_model=list[str])
def list_queries():
    """Return all available query names."""
    return list(QUERIES.keys())


@router.get("/{query_name}")
def run_named_query(query_name: str, db: Session = Depends(get_db)):
    """Run any analytics query dynamically by name."""
    if query_name not in QUERIES:
        raise HTTPException(status_code=404, detail=f"Query '{query_name}' not found")

    sql = text(QUERIES[query_name])
    result = db.execute(sql).mappings().all()
    return {"query": query_name, "rows": result}
