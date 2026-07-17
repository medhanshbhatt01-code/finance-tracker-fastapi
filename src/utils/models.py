from sqlalchemy import Column,Integer,String,ForeignKey,Float
from src.utils.db import Base
class Expenses(Base):
    __tablename__ = "expenses"

    id = Column(Integer,primary_key=True)
    title = Column(String)
    amount = Column(Float)
    category = Column(String)
    user_id = Column(Integer,nullable=True)    