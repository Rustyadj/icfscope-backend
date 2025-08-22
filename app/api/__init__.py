from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
import os

router = APIRouter()

@router.get("/")
def api_root():
    return {"message": "ICFScope API is running", "version": "1.0.0"}

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "database": "connected" if os.getenv("DATABASE_URL") else "not configured",
        "redis": "connected" if os.getenv("REDIS_URL") else "not configured"
    }

@router.get("/manufacturers")
def get_manufacturers():
    """Get list of ICF manufacturers"""
    manufacturers = [
        {
            "id": 1,
            "name": "Nudura",
            "description": "Leading ICF manufacturer with innovative designs",
            "core_sizes": ["6\"", "8\"", "10\"", "12\""]
        },
        {
            "id": 2,
            "name": "Fox Blocks",
            "description": "Premium ICF systems for residential and commercial",
            "core_sizes": ["6\"", "8\"", "10\"", "12\""]
        },
        {
            "id": 3,
            "name": "BuildBlock",
            "description": "Versatile ICF solutions for all construction types",
            "core_sizes": ["6\"", "8\"", "10\"", "12\"", "14\""]
        },
        {
            "id": 4,
            "name": "Logix",
            "description": "High-performance ICF systems",
            "core_sizes": ["6\"", "8\"", "10\"", "12\""]
        },
        {
            "id": 5,
            "name": "Amvic",
            "description": "Innovative building solutions",
            "core_sizes": ["6\"", "8\"", "10\"", "12\""]
        }
    ]
    return {"manufacturers": manufacturers}

@router.post("/auth/register")
def register_user(user_data: Dict[str, Any]):
    """Register a new user"""
    return {"message": "User registration endpoint", "status": "coming_soon"}

@router.post("/auth/login")
def login_user(credentials: Dict[str, Any]):
    """Login user"""
    return {"message": "User login endpoint", "status": "coming_soon"}

@router.get("/projects")
def get_projects():
    """Get user projects"""
    return {"projects": [], "message": "Projects endpoint ready"}

@router.post("/projects")
def create_project(project_data: Dict[str, Any]):
    """Create a new project"""
    return {"message": "Project creation endpoint", "status": "coming_soon"}
