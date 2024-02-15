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

@app.get("/predict")
async def predict(data: Data):
    return int(model.predict_diabetes(**data.model_dump())[0])