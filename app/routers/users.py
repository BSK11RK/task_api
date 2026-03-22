# ユーザーAPI
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas, auth


router = APIRouter(prefix="/users", tags=["users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    db_user = db.query(models.User).filter(
        models.User.email == form_data.username
    ).first()
    if not db_user or db_user.password != form_data.password:
        return {"error": "Invalid credentials"}
    
    token = auth.create_access_token({"sub": db_user.email})
    return {"access_token": token}