import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db

# banco separado só pra testes
engine_test = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
TestSession = sessionmaker(bind=engine_test)

def override_get_db():
    db = TestSession()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine_test)
    yield
    Base.metadata.drop_all(bind=engine_test)

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Estudar FastAPI", "priority": "high"})
    assert response.status_code == 201
    assert response.json()["title"] == "Estudar FastAPI"

def test_list_tasks():
    client.post("/tasks/", json={"title": "Tarefa 1"})
    client.post("/tasks/", json={"title": "Tarefa 2"})
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_task_not_found():
    response = client.get("/tasks/999")
    assert response.status_code == 404

def test_update_task():
    create = client.post("/tasks/", json={"title": "Original"})
    task_id = create.json()["id"]
    response = client.patch(f"/tasks/{task_id}", json={"completed": True})
    assert response.json()["completed"] is True

def test_delete_task():
    create = client.post("/tasks/", json={"title": "Deletar"})
    task_id = create.json()["id"]
    client.delete(f"/tasks/{task_id}")
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404