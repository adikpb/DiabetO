from contextlib import asynccontextmanager

import flet.fastapi as flet_fastapi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from . import model2


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
    print(app.__class__)
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

api = FastAPI()


@api.post("/")
async def predict(data: Data):
    return {"outcome": bool(model2.predict_diabetes(**data.model_dump())[0])}


app.mount("/predict", api)
