from sqlalchemy import Column, Integer, Boolean, Text #class로 정의
from database import Base

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(Text)
    completed = Column(Boolean, default=False) 
