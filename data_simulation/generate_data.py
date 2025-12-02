# data_simulation/generate_data.py
from faker import Faker
import pandas as pd
import random
from datetime import date, datetime, timedelta
import os

OUT_DIR = "data_simulation"
os.makedirs(OUT_DIR, exist_ok=True)

fake = Faker()

CATEGORIES = [
    "Groceries", "Transport", "Bills", "Entertainment", "Travel",
    "Dining", "Subscription", "Gifts", "Health", "Education"
]
PAYMENT_MODES = ["Cash", "Credit Card", "Debit Card", "UPI", "NetBanking"]

def generate_month(year: int, month: int, n: int = 500):
    rows = []
    start = date(year, month, 1)
    # compute last day of month
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    days = (next_month - start).days

    for _ in range(n):
        tx_date = start + timedelta(days=random.randint(0, days - 1))
        category = random.choice(CATEGORIES)
        payment_mode = random.choice(PAYMENT_MODES)
        description = fake.sentence(nb_words=6)
        # realistic amounts by category
        base = {
            "Groceries": (20, 300),
            "Transport": (5, 100),
            "Bills": (50, 2000),
            "Entertainment": (50, 500),
            "Travel": (100, 5000),
            "Dining": (20, 400),
            "Subscription": (5, 50),
            "Gifts": (10, 1000),
            "Health": (10, 2000),
            "Education": (50, 5000)
        }[category]
        amount = round(random.uniform(*base), 2)
        # small chance of cashback
        cashback = round(amount * random.choice([0, 0.01, 0.02, 0.05]) if random.random() < 0.25 else 0.0, 2)

        rows.append([tx_date.isoformat(), category, payment_mode, description, amount, cashback])
    df = pd.DataFrame(rows, columns=["date", "category", "payment_mode", "description", "amount_paid", "cashback"])
    return df

def main(year=2025, per_month=500):
    for m in range(1, 13):
        df = generate_month(year, m, n=per_month)
        fname = os.path.join(OUT_DIR, f"expenses_{m:02}.csv")
        df.to_csv(fname, index=False)
        print(f"Wrote {fname} ({len(df)} rows)")

if __name__ == "__main__":
    main()
