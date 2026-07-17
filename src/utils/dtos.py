from pydantic import BaseModel

class expensecreate(BaseModel):
    title:str
    amount:float
    category:str

class expenseresponse(BaseModel):
    id:int
    title:str
    amount:float
    category:str
    user_id:int|None=0


        