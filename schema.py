from ctypes.wintypes import BOOL
from datetime import datetime
from pydantic import BaseModel

class Users(BaseModel):
    id = int
    fname = str
    lname = str
    email = str
    password = str
    CreateDate = datetime
    UpdateDate = datetime
    LastLoginDate = datetime
    status: bool
    class Config:
        orm_mode = True
