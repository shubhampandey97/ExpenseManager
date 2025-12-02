import streamlit as st
from utils.layout import company_sidebar, check_auth

st.set_page_config(page_title="Profile", page_icon="👤")

check_auth()
page = company_sidebar()

st.title("👤 Profile")

st.markdown("**User:** Shubh Example")
st.markdown("**Role:** Employee")
st.markdown("**Email:** shubh@example.com")

with st.expander("🪪 Tokens"):
    st.json({
        "access_token": st.session_state.get("access_token"),
        "refresh_token": st.session_state.get("refresh_token"),
    })

