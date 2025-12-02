# db/test_sqlalchemy.py
from sqlalchemy import create_engine, text
from config import DB_CONFIG

DB_URL = (
    f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

try:
    engine = create_engine(DB_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT DATABASE();"))
        print("✅ Connected to:", result.scalar())
except Exception as e:
    print("❌ SQLAlchemy connection failed:", e)
