from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    # role = Column(String(50), default="employee")  # 👈 NEW
    created_at = Column(DateTime, server_default=func.now())

    expenses = relationship("Expense", back_populates="user")

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date)
    category = Column(String(50))
    payment_mode = Column(String(50))
    description = Column(String(255))
    amount_paid = Column(DECIMAL(10, 2))
    cashback = Column(DECIMAL(10, 2))
    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="expenses")
