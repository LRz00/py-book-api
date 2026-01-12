from fastapi import APIRouter, Depends
from app.services.auth import hash_password, create_token
from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from fastapi.exceptions import HTTPException
from app.services.auth import veryfy_password, create_token, hash_password

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", tags=["Auth"], summary="Register a new user")
def register(data: UserCreate, db: SessionLocal = Depends(get_db)):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    
    user = User(
        email = data.email,
        password=hash_password(data.password)
    )
    db.add(user)
    db.commit()
    return {"message": "User registered successfully"}


@router.post("/login", tags=["Auth"], summary="Login a user")
def login(data: UserLogin, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user or not veryfy_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token(user.id)
    return {"token": token}