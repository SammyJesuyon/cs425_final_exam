# FastAPI Exam Boilerplate

A reusable layered FastAPI application using SQLite and SQLAlchemy. It is designed to be easy to adapt during a software engineering exam.

## Architecture

```text
Client / Swagger
        ↓
FastAPI Route
        ↓
Service / Business Logic
        ↓
Repository / Data Access
        ↓
SQLAlchemy Model
        ↓
SQLite Database
```

## Technologies

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Pytest

## Project Structure

```text
fastapi-exam-boilerplate/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── repositories.py
│   ├── services.py
│   └── exceptions.py
├── tests/
│   └── test_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```
