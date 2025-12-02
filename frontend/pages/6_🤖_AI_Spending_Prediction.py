# frontend/pages/7_📊_AI_Category_Predictions.py
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from utils.layout import company_sidebar, check_auth
from utils.api_client import get_headers

st.set_page_config(page_title="AI Category Predictions", page_icon="📊", layout="wide")

check_auth()
page = company_sidebar()

st.title("📊 AI-Powered Category-wise Predictions")

API_BASE_URL = "http://127.0.0.1:8000/predict/spending"

try:
    res = requests.get(API_BASE_URL, headers=get_headers())
    if res.status_code == 200:
        data = res.json()
        st.success("✅ Predictions generated successfully!")

        overall = data["overall_predicted_spending"]
        st.metric("Predicted Total Spending (Next Month)", f"₹{overall:,.2f}")

        df = pd.DataFrame(data["categories"])
        st.subheader("📂 Category-wise Forecasts")

        # Trend arrow + color
        df["Trend Arrow"] = df["trend"].apply(lambda x: "⬆️" if x == "up" else "⬇️")
        df["Trend"] = df["trend"].str.capitalize()

        st.dataframe(df[["category", "last_month_spending", "predicted_next_month", "Trend Arrow", "Trend"]],
                     use_container_width=True)

        # 📈 Visualization
        fig = px.bar(
            df,
            x="category",
            y=["last_month_spending", "predicted_next_month"],
            barmode="group",
            title="Last Month vs Predicted Spending by Category",
            labels={"value": "Amount (₹)", "variable": "Type"},
            height=500,
        )
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.error(f"❌ API error: {res.text}")

except Exception as e:
    st.error(f"⚠️ Failed to connect to prediction API: {e}")
