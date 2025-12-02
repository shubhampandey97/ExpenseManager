from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.db import crud
from app.schemas.expense_schema import ExpenseCreate, ExpenseOut
from typing import List
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/expenses", response_model=List[ExpenseOut])
def read_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user=Depends(get_current_user) ):
    return crud.get_expenses(db, skip=skip, limit=limit)

@router.post("/expenses", response_model=ExpenseOut)
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud.create_expense(db, expense)
