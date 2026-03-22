# APIの入出力定義（Pydantic）
from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str
    
    
class UserResponse(BaseModel):
    id: int
    email: str
    
    class Config:
        from_attributes = True


class TaskBase(BaseModel):
    title: str
    
    
class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    completed: bool
    
    
class TaskResponse(TaskBase):
    id: int
    completed: bool
    
    class Config:
        from_attributes = True