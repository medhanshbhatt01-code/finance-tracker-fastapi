from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from src.utils.dtos import expensecreate,expenseresponse
from src.utils.db import get_db
from typing import List
from src.utils.controller import create_new_expense,fetch_all_expenses,sum_expenses


router = APIRouter(prefix='/expenses',tags=['Expenses'])

@router.post('/create_sum',response_model=expenseresponse)
def create_exppenses(body:expensecreate,user_id:int,db:Session = Depends(get_db)):
    return create_new_expense(body=body,db=db,user_id=user_id)

@router.get('/get_expense',response_model=List[expenseresponse])
def fetch_expense(user_id:int,db:Session= Depends(get_db)):
    return fetch_all_expenses(db=db,user_id=user_id)

@router.get('/total_sum',response_model=float)
def sum_expense(user_id:int,db:Session=Depends(get_db)):
    return sum_expenses(user_id=user_id,db=db)


