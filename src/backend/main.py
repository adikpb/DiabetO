from fastapi import FastAPI
from pydantic import BaseModel
import flet_fastapi

from . import model2
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


class Data(BaseModel):
    gender: int
    age: float
    hypertension: int
    heart_diseases: int
    smoking_history: int
    bmi: float
    HbA1c_level: float
    blood_glucose_level: float


@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
async def predict(data: Data):
    return {"outcome": bool(model2.predict_diabetes(**data.model_dump())[0])}
