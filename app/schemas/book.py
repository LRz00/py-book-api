from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    status: str

class BookResponse(BookCreate):
    id: int