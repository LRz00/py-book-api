from enum import Enum
from pydantic import BaseModel
class Status(Enum):
    WANT_TO_READ = "want to read"
    READING = "reading"
    READ = "read"
class BookCreate(BaseModel):
    title: str
    author: str
    status: Status
class BookResponse(BookCreate):
    id: int