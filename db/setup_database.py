from connection import get_connection

def setup_database():
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                # Create DB if not exists
                cursor.execute("CREATE DATABASE IF NOT EXISTS PersonalExpenses;")
                cursor.execute("USE PersonalExpenses;")

                # Create users table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        email VARCHAR(120) UNIQUE NOT NULL,
                        password VARCHAR(255) NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)

                # Create expenses table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS expenses (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        user_id INT NOT NULL,
                        date DATE,
                        category VARCHAR(50),
                        payment_mode VARCHAR(50),
                        description TEXT,
                        amount_paid DECIMAL(10,2),
                        cashback DECIMAL(10,2),
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
                    );
                """)

                conn.commit()
                print("✅ Database and tables created successfully!")
        except Exception as e:
            print("❌ Error creating tables:", e)
        finally:
            conn.close()

if __name__ == "__main__":
    setup_database()
