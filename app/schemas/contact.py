from datetime import datetime
from pydantic import BaseModel, EmailStr, constr, ConfigDict


class ContactCreate(BaseModel):
    name: constr(min_length=1, max_length=200)
    email: EmailStr
    message: constr(min_length=1)


class ContactRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    name: str
    email: EmailStr
    message: str
    created_at: datetime

