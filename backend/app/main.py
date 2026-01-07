from fastapi import FastAPI
from app.api.v1 import diet_plan
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # For MVP only. In production, use your frontend URL.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app = FastAPI(title="AI Diet Planner MVP")

app.include_router(diet_plan.router, prefix="/api/v1")

# @app.get("/")
# def read_root():
#     return {"status": "Backend is running"}