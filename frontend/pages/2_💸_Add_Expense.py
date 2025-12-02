# frontend/pages/2_💸_Add_Expense.py
import streamlit as st
from utils.layout import company_sidebar, check_auth
from utils.api_client import add_expense

st.set_page_config(page_title="Add Expense", page_icon="💸")

check_auth()
page = company_sidebar()

st.title("💸 Add a New Expense")

with st.form("expense_form"):
    date = st.date_input("Date")
    category = st.text_input("Category")
    payment_mode = st.selectbox("Payment Mode", ["Cash", "Card", "UPI", "NetBanking"])
    description = st.text_area("Description")
    amount_paid = st.number_input("Amount Paid", min_value=0.0)
    cashback = st.number_input("Cashback", min_value=0.0)
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        if not category or amount_paid <= 0:
            st.error("Please fill all required fields correctly.")
        else:
            data = {
                "date": str(date),
                "category": category,
                "payment_mode": payment_mode,
                "description": description,
                "amount_paid": amount_paid,
                "cashback": cashback,
            }
            if add_expense(data):
                st.success("Expense added successfully!")
            else:
                st.error("Failed to add expense.")