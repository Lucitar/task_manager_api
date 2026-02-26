from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.repositories.task_repository import TaskRepository
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])

def get_service(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(TaskRepository(db))

@router.get("/", response_model=list[TaskResponse])
def list_tasks(completed: Optional[bool] = Query(None), service: TaskService = Depends(get_service)):
    return service.list_tasks(completed)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, service: TaskService = Depends(get_service)):
    return service.get_task(task_id)

@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(data: TaskCreate, service: TaskService = Depends(get_service)):
    return service.create_task(data)

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data: TaskUpdate, service: TaskService = Depends(get_service)):
    return service.update_task(task_id, data)

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, service: TaskService = Depends(get_service)):
    service.delete_task(task_id)