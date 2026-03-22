from fastapi import FastAPI, Depends
from app.database import engine
from app import models
from app.routers import tasks, users
import os


os.makedirs("data", exist_ok=True)

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(tasks.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "Task API is running"}