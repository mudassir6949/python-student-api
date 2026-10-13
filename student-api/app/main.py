from fastapi import FastAPI

from app.database import Base, engine
from app.models import Student
from app.routes import router


# Create database tables
Base.metadata.create_all(
    bind=engine
)


# Create FastAPI application
app = FastAPI(
    title="Student Management API",
    description="A small Student Management API built with FastAPI",
    version="1.0.0"
)


# Connect student routes to the FastAPI application
app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Student Management API is running",
        "version": "1.0.0"
    }