import pandas as pd
import streamlit as st
from catboost import CatBoostClassifier
from misc import encode

model = CatBoostClassifier()
model.load_model('./weights/model')

st.title('Titanic disaster')
gender = st.selectbox('Выберите пол:', ['Муж', 'Жен'])
age = int(st.number_input('Выберите возраст:'))
with_family = st.selectbox('У пассажира были родственники на борту?', ['Да', 'Нет'])
pclass = st.selectbox('Выберите класс:', [1, 2, 3])
embarked = st.selectbox('Выберите порт отправления:', ['Cherbourg', 'Queenstown', 'Southampton'])
fare = st.number_input('Укажите стоимость билета:')
gender, with_family, pclass, embarked = encode(gender, with_family, pclass, embarked)


def predict():
    """
    :return: Возвращает результат работы модели
    """
    X = pd.DataFrame(columns=['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'WithFamily'],
                     data=[[pclass, gender, age, fare, embarked, with_family]])
    pred = model.predict(X)[0]
    if pred == 1:
        st.success('Пассажир выжил')
    else:
        st.error('Пассажир погиб')


st.button('Предсказать', on_click=predict)
