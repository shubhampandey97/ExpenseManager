import streamlit as st
import pandas as pd
from utils.layout import company_sidebar, check_auth
from utils.api_client import fetch_expenses

st.set_page_config(page_title="Expense History", page_icon="📅", layout="wide")

check_auth()
page = company_sidebar()

st.title("📅 Expense History")

expenses = fetch_expenses()
if expenses:
    df = pd.DataFrame(expenses)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(by="date", ascending=False)

    st.dataframe(df, use_container_width=True)

    with st.expander("📊 Summary by Category"):
        st.bar_chart(df.groupby("category")["amount_paid"].sum())

    with st.expander("💰 Monthly Trend"):
        monthly = df.groupby(df["date"].dt.to_period("M"))["amount_paid"].sum()
        st.line_chart(monthly)
else:
    st.info("No expenses found. Add your first one from the sidebar.")
