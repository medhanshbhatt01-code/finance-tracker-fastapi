from fastapi import FastAPI
from src.utils.db import engine, Base 
from src.utils.dtos import expensecreate,expenseresponse
from src.expenses.router import router


Base.metadata.create_all(bind=engine)
app = FastAPI()

app = FastAPI(title="Personal Finance Tracker",
    description="An API to track personal expenses and spend totals.",
    version="1.0.0")

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to your Personal Finance Tracker API!"}
