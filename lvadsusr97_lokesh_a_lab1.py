# -*- coding: utf-8 -*-
"""LVADSUSR97_lokesh_A_lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZLuDDxJ4yBAMT-Vijd2ELHtjYLmwT6kH
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

df=pd.read_csv("/content/sample_data/expenses.csv")
df

df.isnull()

df.isnull().sum()

df.dropna(inplace=True)

label_encoder=LabelEncoder()
df['sex']=label_encoder.fit_transform(df['sex'])
df['smoker']=label_encoder.fit_transform(df['smoker'])
df['region']=label_encoder.fit_transform(df['region'])
df

df.drop_duplicates()

x=df.iloc[:,0:3:2]
y=df.iloc[:,-1:]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=42)

model_p=LinearRegression()
model_p=model_p.fit(x_train,y_train)
model_predic=model_p.predict(x_test)
print(model_predic)
#model_accuracy=accuracy_score(model_predic,y_test)
mse=mean_squared_error(model_predic,y_test)
print("...........")
print("the mean squared error is ",mse)
mae=mean_squared_error(model_predic,y_test)
print("...........")
print("the mae is",mae)