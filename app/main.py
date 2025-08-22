from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(title="ICFScope Backend")

app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "ICFScope Backend API is running"}
