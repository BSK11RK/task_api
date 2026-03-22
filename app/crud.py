# DB操作（SQLAlchemy）
from sqlalchemy.orm import Session
from app import models


def get_tasks(db: Session):
    return db.query(models.Task).all()


def create_task(db: Session, title: str):
    task = models.Task(title=title)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def update_task(db: Session, task_id: int, completed: bool):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        return None
    task.completed = completed
    db.commit()
    return task


def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task