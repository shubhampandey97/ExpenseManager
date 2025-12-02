# frontend/pages/1_📊_Dashboard.py
import streamlit as st
import pandas as pd
from utils.layout import company_sidebar, check_auth
from utils.api_client import list_analytics_queries, fetch_analytics

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

# Check user auth
check_auth()
page = company_sidebar()

st.title("📊 Expense Analytics Dashboard")

st.markdown("Explore your expenses through dynamic analytics powered by FastAPI and MySQL.")

# --- Fetch available analytics queries from backend ---
with st.spinner("Fetching available analytics..."):
    query_list = list_analytics_queries()

if not query_list:
    st.error("No analytics queries available or API not reachable.")
    st.stop()

# --- Sidebar: Choose a report dynamically ---
selected_query = st.sidebar.selectbox(
    "📈 Select an Analytics Report",
    query_list,
    index=0
)

st.subheader(f"Analytics Report: `{selected_query}`")

# --- Fetch analytics data ---
with st.spinner(f"Running query `{selected_query}`..."):
    data = fetch_analytics(selected_query)

if not data:
    st.warning("No data returned for this report.")
    st.stop()

df = pd.DataFrame(data)

# --- Display results ---
st.dataframe(df, use_container_width=True)

# --- Visualize intelligently ---
if df.shape[1] == 2:  # For most group-by queries
    col1, col2 = st.columns([2, 3])
    with col2:
        try:
            st.bar_chart(df.set_index(df.columns[0]))
        except Exception:
            st.line_chart(df.set_index(df.columns[0]))
elif "month" in df.columns or "date" in df.columns:
    st.line_chart(df.set_index(df.columns[0]))
else:
    st.info("Showing tabular data only (no suitable numeric column for chart).")

st.success("✅ Data loaded successfully!")
