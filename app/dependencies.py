from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from app.services.auth import decode_token

security = HTTPBearer()

def get_current_user(token: HTTPBearer = Depends(security)):
    user_id = decode_token(token.credentials)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user_id
    