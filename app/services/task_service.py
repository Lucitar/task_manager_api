from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate
from app.models.task import Task
from fastapi import HTTPException
from typing import Optional

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def list_tasks(self, completed: Optional[bool] = None) -> list[Task]:
        return self.repository.get_all(completed)

    def get_task(self, task_id: int) -> Task:
        task = self.repository.get_by_id(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        return task

    def create_task(self, data: TaskCreate) -> Task:
        return self.repository.create(data)

    def update_task(self, task_id: int, data: TaskUpdate) -> Task:
        task = self.get_task(task_id)
        return self.repository.update(task, data)

    def delete_task(self, task_id: int) -> None:
        task = self.get_task(task_id)
        self.repository.delete(task)