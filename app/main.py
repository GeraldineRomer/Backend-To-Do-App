from fastapi import FastAPI
from app.api.task_routes import router as task_router
from app.api.user_routes import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine
from app.models import task_model, user_model

task_model.Base.metadata.create_all(bind=engine)
user_model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tareas API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",  # Angular
        "http://localhost:3000",  # React (por si acaso)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)
app.include_router(user_router)
