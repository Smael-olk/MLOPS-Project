from fastapi import FastAPI
from app.model.model import predict_loan
from app.model.model import sanitize
from pydantic import BaseModel

class ListIn(BaseModel):
    L : str

class PredictionOut(BaseModel):
    Loan_prediction: str
app = FastAPI()

@app.get("/")
async def root():
    return {"Health_check":"OK"}

@app.post("/predict")
def predict(payload: ListIn):
    predictionlist=sanitize(payload.L)
    print(predictionlist)
    prediction=predict_loan(predictionlist)
    return prediction 