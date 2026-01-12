from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str

class UserLogin(UserCreate):
    email: EmailStr