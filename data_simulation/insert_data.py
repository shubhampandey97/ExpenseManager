import pymysql
import pandas as pd
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from config import DB_CONFIG

conn = pymysql.connect(**DB_CONFIG)
cursor = conn.cursor()

for month in range(1, 13):
    # df = pd.read_csv(f"data_simulation/expenses_{month}.csv")
    
    file_path = f"data_simulation/expenses_{month:02}.csv"
    print(f"Reading file: {file_path}")
    df = pd.read_csv(file_path)
    

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO expenses (date, category, payment_mode, description, amount_paid, cashback)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, tuple(row))
    
    conn.commit()

cursor.close()
conn.close()
print("Data inserted successfully!")
