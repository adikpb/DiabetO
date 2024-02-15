from fastapi import FastAPI
from pydantic import BaseModel
import flet_fastapi

from . import model
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

class Data(BaseModel):
    pregnancies: int
    glucose: float
    bloodpressure: float
    skinthickness: float
    insulin: float
    bmi: float
    diabetespedigreefunction: float
    age: int

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
    return {"outcome": bool(model.predict_diabetes(**data.model_dump())[0])}