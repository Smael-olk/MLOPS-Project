from fastapi import FastAPI
from app.model.model import predict_loan
from app.model.model import sanitize
from pydantic import BaseModel
from prometheus_client import Counter, make_asgi_app
survived_counter = Counter("survived", "Counter for survived")
not_survived_counter = Counter("not_survived", "Counter for not survived")

class ListIn(BaseModel):
    L : str

class PredictionOut(BaseModel):
    Loan_prediction: int

app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


@app.get("/")
async def root():
    return {"Health_check":"OK"}

@app.post("/predict")
def predict(payload: ListIn):
    predictionlist=sanitize(payload.L)
    print(predictionlist)
    prediction=predict_loan(predictionlist)
    survived = (prediction == 1)
    if survived:
        survived_counter.inc()
    else:
        not_survived_counter.inc()
    return survived


