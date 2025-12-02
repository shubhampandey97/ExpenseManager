import streamlit as st
import pandas as pd
import requests
from utils.layout import company_sidebar, check_auth
from utils.api_client import get_headers

API_BASE_URL = "http://127.0.0.1:8000/api"

st.set_page_config(page_title="Analytics", page_icon="📈", layout="wide")

check_auth()
page = company_sidebar()

st.title("📈 Expense Analytics Dashboard")

# Fetch all query names dynamically
res = requests.get(f"{API_BASE_URL}/analytics/list", headers=get_headers())
if res.status_code != 200:
    st.error("Failed to load available analyses.")
    st.stop()

query_names = res.json()
query_name = st.selectbox("Select an analysis:", query_names)

if st.button("Run Analysis"):
    with st.spinner("Running analysis..."):
        res = requests.get(f"{API_BASE_URL}/analytics/{query_name}", headers=get_headers())
        if res.status_code == 200:
            data = res.json()["rows"]
            if not data:
                st.info("No data returned for this query.")
            else:
                df = pd.DataFrame(data)
                st.success(f"✅ Query '{query_name}' executed successfully")
                st.dataframe(df, use_container_width=True)

                # Auto-visualize if possible
                numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
                if len(numeric_cols) >= 1 and len(df.columns) >= 2:
                    st.bar_chart(df.set_index(df.columns[0])[numeric_cols[0]])
        else:
            st.error(f"Error {res.status_code}: {res.text}")
