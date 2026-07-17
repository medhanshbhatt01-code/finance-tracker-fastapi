from src.utils.models import Expenses
from sqlalchemy.orm import Session
from src.utils.dtos import expensecreate
from sqlalchemy import func

def create_new_expense(db:Session,body:expensecreate,user_id:int):
    data = body.model_dump()
    new_expense = Expenses(title = data["title"],
                           amount = data["amount"],
                           category = data["category"],
                           user_id = user_id)
    
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

def fetch_all_expenses(db:Session,user_id:int):
    tasks = db.query(Expenses).filter(user_id == Expenses.user_id).all()
    return tasks

def sum_expenses(db:Session,user_id:int):
    total_amount = db.query(func.sum(Expenses.amount)).filter(Expenses.user_id == user_id).scalar()
    return total_amount or 0






    