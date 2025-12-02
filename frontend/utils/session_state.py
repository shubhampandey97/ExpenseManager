# frontend/utils/session_state.py
import streamlit as st

def init_session_state():
    if "access_token" not in st.session_state:
        st.session_state["access_token"] = None
    if "refresh_token" not in st.session_state:
        st.session_state["refresh_token"] = None
    if "is_logged_in" not in st.session_state:
        st.session_state["is_logged_in"] = False
