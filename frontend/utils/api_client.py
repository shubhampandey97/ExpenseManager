# frontend/utils/api_client.py
import requests
import streamlit as st
from datetime import datetime, timedelta

API_BASE_URL = "http://127.0.0.1:8000/api"

# ---------------- AUTH & TOKEN MANAGEMENT ---------------- #

def login_user(email: str, password: str):
    """Authenticate user via FastAPI and store tokens in Streamlit session."""
    data = {
        "grant_type": "password",
        "username": email,
        "password": password,
    }
    res = requests.post(f"{API_BASE_URL}/login", data=data)
    if res.status_code == 200:
        tokens = res.json()
        st.session_state["access_token"] = tokens["access_token"]
        st.session_state["refresh_token"] = tokens["refresh_token"]
        st.session_state["token_expiry"] = datetime.utcnow() + timedelta(seconds=tokens["expires_in"])
        return True
    else:
        st.error("❌ Invalid login credentials")
        return False


def refresh_access_token():
    """Refresh expired access token using refresh token."""
    refresh_token = st.session_state.get("refresh_token")
    if not refresh_token:
        st.error("⚠️ No refresh token found. Please log in again.")
        return False

    res = requests.post(f"{API_BASE_URL}/refresh", json={"refresh_token": refresh_token})
    if res.status_code == 200:
        tokens = res.json()
        st.session_state["access_token"] = tokens["access_token"]
        st.session_state["token_expiry"] = datetime.utcnow() + timedelta(seconds=tokens["expires_in"])
        return True
    else:
        st.error("🔑 Token refresh failed. Please log in again.")
        return False


def get_headers():
    """Get valid headers with Authorization token."""
    if "access_token" in st.session_state:
        if datetime.utcnow() >= st.session_state.get("token_expiry", datetime.utcnow()):
            refresh_access_token()
        return {"Authorization": f"Bearer {st.session_state['access_token']}"}
    return {}

# ---------------- EXPENSE CRUD ---------------- #

def fetch_expenses():
    """Fetch all expenses."""
    try:
        res = requests.get(f"{API_BASE_URL}/expenses", headers=get_headers())
        res.raise_for_status()
        return res.json()
    except Exception as e:
        st.error(f"❌ Failed to fetch expenses: {e}")
        return []


def add_expense(data: dict):
    """Add a new expense."""
    try:
        res = requests.post(f"{API_BASE_URL}/expenses", json=data, headers=get_headers())
        return res.status_code == 200
    except Exception as e:
        st.error(f"❌ Failed to add expense: {e}")
        return False

# ---------------- ANALYTICS API ---------------- #

def list_analytics_queries():
    """Fetch list of available analytics query names."""
    try:
        res = requests.get(f"{API_BASE_URL}/analytics/list", headers=get_headers())
        if res.status_code == 200:
            return res.json()
        else:
            st.error(f"Error fetching analytics list: {res.text}")
            return []
    except Exception as e:
        st.error(f"❌ Connection error: {e}")
        return []



def fetch_analytics(query_name: str):
    """Run a specific analytics query."""
    try:
        res = requests.get(f"{API_BASE_URL}/analytics/{query_name}", headers=get_headers())
        if res.status_code == 200:
            return res.json()
        else:
            st.error(f"Error fetching {query_name}: {res.text}")
            return []
    except Exception as e:
        st.error(f"❌ Connection error: {e}")
        return []
