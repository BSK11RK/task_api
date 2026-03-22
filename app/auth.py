from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.database import SessionLocal
from app import models


SECRET_KEY = "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")


# DB セッション
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# トークン発行
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# トークン検証
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        return email
    except JWTError:
        return None
    

# 現在のユーザーを取得    
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    email = verify_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user