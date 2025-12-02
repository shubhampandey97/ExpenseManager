# frontend/Home.py
import streamlit as st
from utils.api_client import login_user
from utils.session_state import init_session_state

st.set_page_config(page_title="Expense Manager", page_icon="💰", layout="centered")

init_session_state()

st.title("💼 Company Expense Manager")

if not st.session_state["is_logged_in"]:
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            success = login_user(email, password)
            if success:
                st.session_state["is_logged_in"] = True
                st.success("✅ Login successful! Use the sidebar to navigate.")
else:
    st.success("You are logged in!")
    if st.button("Logout"):
        for key in ["access_token", "refresh_token", "is_logged_in"]:
            st.session_state[key] = None
        st.rerun()
