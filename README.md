# Task Manager API

A RESTful API for managing tasks, built with FastAPI and SQLAlchemy.

## Features

- Create, read, update and delete tasks
- Filter tasks by completion status
- Task priority levels (low, medium, high)
- Input validation with Pydantic
- Unit tests with pytest

## Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- Pytest

## Project Structure

```  
app/  
├── main.py  
├── database.py  
├── models/        # ORM models  
├── schemas/       # Pydantic schemas  
├── repositories/  # Database access layer  
├── services/      # Business logic layer  
└── routers/       # API endpoints  
tests/  
└── test_tasks.py  
```

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/Lucitar/task_manager_api.git
cd task_manager_api
```

**2. Create and activate virtual environment**
```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the server**
```bash
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`  
Interactive docs at `http://localhost:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks/ | List all tasks |
| GET | /tasks/{id} | Get task by id |
| POST | /tasks/ | Create a task |
| PATCH | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

### Filter by status
```
GET /tasks/?completed=false
GET /tasks/?completed=true
```

## Running Tests

```bash
pytest tests/ -v
```

## Architecture

This project follows a layered architecture pattern:

- **Router** → handles HTTP requests and responses
- **Service** → contains business logic
- **Repository** → handles database operations
- **Model** → defines database schema
- **Schema** → handles data validation and serialization