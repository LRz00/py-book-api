from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    status = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))