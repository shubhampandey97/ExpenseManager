# db/connection.py
import pymysql
from config import DB_CONFIG

def get_connection():
    try:
        conn = pymysql.connect(**DB_CONFIG)
        print("✅ Database connection successful!")
        return conn
    except Exception as e:
        print("❌ Database connection failed:", e)
        return None
