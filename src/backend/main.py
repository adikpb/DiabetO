from fastapi import FastAPI
from pydantic import BaseModel

from . import model


class Data(BaseModel):
    pregnancies: int
    glucose: float
    bloodpressure: float
    skinthickness: float
    insulin: float
    bmi: float
    diabetespedigreefunction: float
    age: int

app = FastAPI()

@app.post("/predict")
async def predict(data: Data):
    return bool(model.predict_diabetes(**data.model_dump())[0])