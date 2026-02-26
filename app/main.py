from fastapi import FastAPI
from app.database import Base, engine
from app.routers import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")
app.include_router(tasks.router)