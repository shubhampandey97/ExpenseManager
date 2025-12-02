# db/test_connection.py
from connection import get_connection

conn = get_connection()

if conn:
    with conn.cursor() as cursor:
        cursor.execute("SHOW DATABASES;")
        databases = cursor.fetchall()
        print("📦 Databases:", databases)

        cursor.execute("USE PersonalExpenses;")
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("📋 Tables:", tables)

    conn.close()
