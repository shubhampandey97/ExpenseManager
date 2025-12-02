# frontend/utils/layout.py
import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

# ---------------- AUTH CHECK ---------------- #
def check_auth():
    """Ensure the user is logged in, otherwise redirect to login."""
    if "access_token" not in st.session_state:
        st.warning("🔒 Please log in to access the dashboard.")
        st.switch_page("Home.py")


# ---------------- SIDEBAR LAYOUT ---------------- #
def company_sidebar():
    """Company-style sidebar navigation with icons and session details."""
    with st.sidebar:
        # Company branding
        st.image("https://upload.wikimedia.org/wikipedia/commons/a/ab/Logo_TV_2022.svg", width=180)
        st.markdown("---")

        # Display user info if available
        user_email = st.session_state.get("user_email", "guest@company.com")
        st.markdown(f"👤 **Logged in as:** `{user_email}`")
        if "token_expiry" in st.session_state:
            expires = st.session_state["token_expiry"].strftime("%H:%M:%S")
            st.caption(f"🔑 Token expires at {expires} UTC")

        st.markdown("---")

        # Navigation menu
        selected = option_menu(
            menu_title="Navigation",
            options=[
                "📊 Dashboard",
                "💸 Add Expense",
                "📅 Expense History",
                "👤 Profile",
                "🚪 Logout",
            ],
            icons=["bar-chart-line", "plus-circle", "calendar2-week", "person-circle", "box-arrow-right"],
            menu_icon="list",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#f8f9fa"},
                "icon": {"color": "#0d6efd", "font-size": "20px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#e9ecef",
                },
                "nav-link-selected": {"background-color": "#0d6efd", "color": "white"},
            },
        )

        st.markdown("---")
        st.caption("💼 Expense Manager — v1.0")

    # Handle logout
    if selected == "🚪 Logout":
        for key in ["access_token", "refresh_token", "token_expiry", "user_email"]:
            st.session_state.pop(key, None)
        st.success("✅ You have been logged out.")
        st.switch_page("Home.py")

    return selected
