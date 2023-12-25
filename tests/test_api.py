import requests
from api import Passenger, app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_init():
    passenger = Passenger(pclass=3, gender=1, age=30, fare=7.5, embarked=1, with_family=0)
    assert passenger.pclass == 3
    assert passenger.gender == 1
    assert passenger.age == 30
    assert passenger.fare == 7.5
    assert passenger.embarked == 1
    assert passenger.with_family == 0


def test_api():
    response = requests.post('http://127.0.0.1:8000/predict',
                             json={'pclass': '0',
                                   'gender': '0',
                                   'age': '0',
                                   'fare': '0',
                                   'embarked': '0',
                                   'with_family': '0'})
    assert response.status_code == 200
    assert response.json() == {"predict": "0.0"}
