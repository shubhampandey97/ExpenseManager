from connection import get_connection

def view_data():
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("USE PersonalExpenses;")
                cursor.execute("SELECT * FROM users;")
                users = cursor.fetchall()
                print("👤 Users:")
                for row in users:
                    print(row)

                cursor.execute("SELECT * FROM expenses;")
                expenses = cursor.fetchall()
                print("\n💰 Expenses:")
                for row in expenses:
                    print(row)
        except Exception as e:
            print("❌ Error fetching data:", e)
        finally:
            conn.close()

if __name__ == "__main__":
    view_data()
