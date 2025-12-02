from connection import get_connection
from datetime import date

def insert_sample_data():
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("USE PersonalExpenses;")

                # Insert a sample user
                cursor.execute("""
                    INSERT INTO users (name, email, password)
                    VALUES (%s, %s, %s)
                """, ("John Doe", "john@example.com", "hashed_password_123"))
                user_id = cursor.lastrowid

                # Insert sample expenses for that user
                sample_expenses = [
                    (user_id, date(2025, 11, 1), "Groceries", "Credit Card", "Bought groceries", 250.50, 5.00),
                    (user_id, date(2025, 11, 2), "Transport", "Cash", "Bus ticket", 40.00, 0.00),
                    (user_id, date(2025, 11, 3), "Entertainment", "UPI", "Movie ticket", 300.00, 0.00),
                ]

                cursor.executemany("""
                    INSERT INTO expenses (user_id, date, category, payment_mode, description, amount_paid, cashback)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, sample_expenses)

                conn.commit()
                print("✅ Sample data inserted successfully!")
        except Exception as e:
            print("❌ Error inserting data:", e)
        finally:
            conn.close()

if __name__ == "__main__":
    insert_sample_data()
