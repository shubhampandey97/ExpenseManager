from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class ExpenseBase(BaseModel):
    date: date
    category: str
    payment_mode: str
    description: Optional[str] = None
    amount_paid: float
    cashback: float = 0.0


class ExpenseCreate(ExpenseBase):
    user_id: Optional[int] = None  # Optional for inserts from frontend


class ExpenseOut(ExpenseBase):
    id: int
    user_id: Optional[int] = None  # ✅ make it optional here
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
