import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from catboost import CatBoostClassifier

model = CatBoostClassifier()
try:
    model.load_model('./weights/model')
except Exception:
    model.load_model('../weights/model')

app = FastAPI()


class Passenger(BaseModel):
    pclass: int
    gender: int
    age: int
    fare: float
    embarked: int
    with_family: int


@app.post("/predict")
def predict(passenger: Passenger):
    """
    :param passenger: Параметры пассажира для классификации
    :return: Возвращает статус пассажира, выжил или нет
    """
    X = pd.DataFrame(columns=['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'WithFamily'],
                     data=[[passenger.pclass,
                            passenger.gender,
                            passenger.age,
                            passenger.fare,
                            passenger.embarked,
                            passenger.with_family]])
    print(X)
    return {'predict': str(model.predict(X)[0])}
