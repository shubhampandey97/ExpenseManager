# backend/app/api/predict_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.db.models import Expense
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

router = APIRouter(prefix="/predict", tags=["AI Spending Prediction"])

@router.get("/spending")
def predict_spending(db: Session = Depends(get_db)):
    """AI-based monthly + category-wise spending forecast for next month."""

    user_id = 1  # temporary static user
    expenses = db.query(Expense).filter(Expense.user_id == user_id).all()

    if not expenses:
        raise HTTPException(status_code=404, detail="No expense data found")

    # Prepare DataFrame
    df = pd.DataFrame(
        [{"date": e.date, "category": e.category, "amount": float(e.amount_paid or 0)} 
         for e in expenses if e.date]
    )

    if df.empty:
        raise HTTPException(status_code=404, detail="No valid expense data found")

    df["month"] = pd.to_datetime(df["date"]).dt.to_period("M")

    # Monthly total per category
    grouped = df.groupby(["category", "month"])["amount"].sum().reset_index()

    results = []
    for category, group in grouped.groupby("category"):
        group = group.sort_values("month")
        group["month_index"] = range(len(group))

        if len(group) < 3:
            continue  # skip if not enough data

        X = group["month_index"].values.reshape(-1, 1)
        y = group["amount"].values
        model = LinearRegression()
        model.fit(X, y)

        next_index = np.array([[group["month_index"].max() + 1]])
        predicted = float(model.predict(next_index)[0])
        trend = "up" if model.coef_[0] > 0 else "down"

        results.append({
            "category": category,
            "predicted_next_month": round(predicted, 2),
            "last_month_spending": round(float(group.iloc[-1]["amount"]), 2),
            "trend": trend,
            "months_trained": len(group)
        })

    if not results:
        raise HTTPException(status_code=400, detail="Not enough data for any category")

    # Overall monthly trend (same as before)
    overall = df.groupby("month")["amount"].sum().reset_index()
    overall["month_index"] = range(len(overall))
    model_all = LinearRegression().fit(
        overall["month_index"].values.reshape(-1, 1), overall["amount"].values
    )
    next_total = float(model_all.predict([[overall["month_index"].max() + 1]])[0])

    return {
        "user_id": user_id,
        "overall_predicted_spending": round(next_total, 2),
        "categories": results,
    }
