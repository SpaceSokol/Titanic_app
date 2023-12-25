import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from catboost import CatBoostClassifier

model = CatBoostClassifier()
model.load_model('./weights/model')

app = FastAPI()


class Passenger(BaseModel):
    pclass: int
    gender: int
    age: int
    fare: float
    embarked: int
    with_family: int


@app.post("/predict/")
def predict(passenger: Passenger):
    X = pd.DataFrame(columns=['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'WithFamily'],
                     data=[[passenger.pclass,
                            passenger.gender,
                            passenger.age,
                            passenger.fare,
                            passenger.embarked,
                            passenger.with_family]])
    return model.predict(X)[0]
