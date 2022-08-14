from datetime import datetime
from sqlalchemy import BOOLEAN, Column, Integer, String,DateTime, true
from sqlalchemy_utils import EmailType
import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from database import Base

class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True,index=true)
    fname = Column(String(255))
    lname = Column(String(255))
    email = Column(EmailType)
    password = Column(String(255))
    CreateDate = Column(DateTime,default=datetime.datetime.utcnow)
    UpdateDate = Column(DateTime,default=datetime.datetime.utcnow)
    LastLoginDate = Column(DateTime,default=datetime.datetime.utcnow)
    status = Column(BOOLEAN, default=True)