from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.book import Book
from app.schemas.book import BookCreate
from app.dependencies import get_current_user

router = APIRouter(prefix="/books")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_book(
    data: BookCreate, db: Session = Depends(get_db), 
    user_id:int = Depends(get_current_user)
):
    book = Book(**data.model_dump(), user_id=user_id)
    db.add(book)
    db.commit()
    return book

@router.get("/")
def get_books(
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Book).filter(Book.user_id == user_id).all()


@router.put("/{book_id}")
def update_book(
    book_id: int,
    data: BookCreate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    book = db.query(Book).filter(Book.id == book_id, Book.user_id == user_id).first()

    if book:
        for k, v in data.model_dump().items():
            setattr(book, k, v)
        db.commit()
    
    return book

@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    book = db.query(Book).filter(
        Book.id == book_id,
        Book.user_id == user_id
    ).first()

    if book:
        db.delete(book)
        db.commit()

    return {"message": "Deleted"}

