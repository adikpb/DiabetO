from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv(Path.joinpath(
    Path(__file__).parent.absolute(), Path("diabetes_prediction_dataset.csv")))

X = df[['gender', 'age', 'hypertension', 'heart_disease',
        'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level']]
y = df['diabetes']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=10)

lm = LogisticRegression()
lm.fit(X_train, y_train)


def predict_diabetes(gender, age, hypertension, heart_diseases, smoking_history, bmi, HbA1c_level, blood_glucose_level):
    a = np.array([[gender, age, hypertension, heart_diseases,
                 smoking_history, bmi, HbA1c_level, blood_glucose_level]])
    new_pred = lm.predict(a)
    return (new_pred)
