from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Configuration(Base):
    __tablename__ = "configurations"
    
    id = Column(Integer, primary_key=True)
    service = Column(String)
    adapter = Column(String)
    version = Column(String)