from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, books

Base.metadata.create_all(bind=engine)

app = FastAPI(title= "Book API")

app.include_router(auth.router)
app.include_router(books.router)
