from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from typing import Optional

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, completed: Optional[bool] = None) -> list[Task]:
        query = self.db.query(Task)
        if completed is not None:
            query = query.filter(Task.completed == completed)
        return query.all()

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def create(self, data: TaskCreate) -> Task:
        task = Task(**data.model_dump())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update(self, task: Task, data: TaskUpdate) -> Task:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(task, field, value)
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete(self, task: Task) -> None:
        self.db.delete(task)
        self.db.commit()