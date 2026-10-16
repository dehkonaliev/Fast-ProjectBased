from sqlalchemy import String, Integer, Column
from app.db import Base

class User(Base):
    __tablename__="users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)