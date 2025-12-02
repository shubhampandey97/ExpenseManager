````markdown
# 💰 ExpenseManager

A full-stack personal expense management system built with FastAPI, MySQL, and Streamlit.
It enables secure authentication, expense tracking, and rich analytics dashboards — designed with company-grade standards and modular structure.

## 🚀 Features

✅ Secure authentication (OAuth2 + JWT refresh)
✅ CRUD for expenses (Create / Read / Update / Delete)
✅ Dynamic SQL-based analytics
✅ Streamlit frontend with session-based auth
✅ Modular backend architecture (FastAPI)
✅ Auto-refresh token mechanism
✅ Company-grade structure (backend + frontend separation)


## 🏗️ Project Structure
ExpenseManager/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth_routes.py
│   │   │   ├── user_routes.py
│   │   │   ├── analytics_routes.py
│   │   │   └── routes.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   └── security.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   └── expense.py
│   │   ├── utils/
│   │   │   └── query_loader.py
│   │   ├── sql/
│   │   │   └── queries.sql
│   │   └── main.py
│   ├── requirements.txt
│   └── alembic.ini
│
├── frontend/
│   ├── Home.py
│   ├── pages/
│   │   ├── 1_📊_Dashboard.py
│   │   ├── 2_➕_Add_Expense.py
│   │   ├── 3_👤_Profile.py
│   │   └── 5_📈_Analytics.py
│   ├── utils/
│   │   ├── api_client.py
│   │   └── layout.py
│   └── requirements.txt
│
├── data_simulation/
│   ├── expenses_01.csv
│   └── insert_data.py
│
├── setup_database.sql
├── queries.sql
├── .gitignore
└── README.md

## ⚙️ Installation Guide

### 🧩 1. Clone the Repository
git clone https://github.com/shubhampandey97/ExpenseManager.git
cd ExpenseManager

### 🐍 2. Create & Activate Virtual Environment
python -m venv expense_manager
expense_manager\Scripts\activate

### 📦 3. Install Dependencies

Backend:
cd backend
pip install -r requirements.txt

Frontend:
cd ../frontend
pip install -r requirements.txt

### 💾 4. Configure Database

#### 4.1 Create Database
CREATE DATABASE expense_manager;

#### 4.2 Update your .env file
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=expense_manager
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

### ⚡ 5. Run Backend (FastAPI)
cd backend
uvicorn app.main:app --reload

### 🎨 6. Run Frontend (Streamlit)
cd ../frontend
streamlit run Home.py

## 📈 Analytics Queries

Dynamic analytics queries are stored in:
backend/app/sql/queries.sql

Access via API:
GET /api/analytics/total_expense_per_month

## 🧠 Authentication Flow
| Step | Description                 | Endpoint        |
| ---- | --------------------------- | --------------- |
| 1    | Login with email/password   | `/api/login`    |
| 2    | Get access + refresh tokens | Response        |
| 3    | Streamlit stores tokens     | `api_client.py` |
| 4    | Auto-refresh on expiry      | `/api/refresh`  |

## 🧩 Tech Stack

| Layer     | Technology                     |
| --------- | ------------------------------ |
| Backend   | FastAPI + SQLAlchemy + PyMySQL |
| Frontend  | Streamlit                      |
| Database  | MySQL                          |
| Auth      | OAuth2 + JWT                   |
| Analytics | SQL-based                      |


## 🧪 Developer Notes

Always start backend before frontend
Use .env for all sensitive configs
Each SQL query in queries.sql must have a unique -- name: tag
Use Alembic for schema migrations

## 🧑‍💻 Author
Shubh
💼 Full-Stack Data Developer
📧 shubh@example.com
(test123)

## 📄 License
MIT License © 2025 — ExpenseManager Project
