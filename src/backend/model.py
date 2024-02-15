import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('./Healthcare-Diabetes.csv')

X = df[['Pregnancies', 'Glucose', 'BloodPressure','SkinThickness', 'Insulin','BMI','DiabetesPedigreeFunction','Age']]
y = df['Outcome']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.4,random_state=10)

lm = LogisticRegression()
lm.fit(X_train,y_train)

def predict_ans(pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age):
    a=np.array([[pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age]])
    new_pred= lm.predict(a)
    return(new_pred)






