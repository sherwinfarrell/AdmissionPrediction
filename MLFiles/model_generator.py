import pandas as pd
import os
os.getcwd() 
        

df = pd.read_csv("Admission_Predict_Ver1.1.csv")
df.head()

df = df.drop(['Serial No.'], axis=1)
df.isnull().sum()

from sklearn.model_selection import train_test_split

X = df.drop(['Chance of Admit '], axis=1)
y = df['Chance of Admit ']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.20, shuffle=False)

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import Lasso,Ridge,BayesianRidge,ElasticNet,HuberRegressor,LinearRegression,LogisticRegression,SGDRegressor
from sklearn.metrics import mean_squared_error
import pickle
models = [['DecisionTree',DecisionTreeRegressor()],
           ['Linear Regression', LinearRegression()],
           ['RandomForest',RandomForestRegressor()],
           ['KNeighbours', KNeighborsRegressor(n_neighbors = 2)],
           ['SVM', SVR()],
           ['AdaBoostClassifier', AdaBoostRegressor()],
           ['GradientBoostingClassifier', GradientBoostingRegressor()],
           
           ['Lasso', Lasso()],
           ['Ridge', Ridge()],
           ['BayesianRidge', BayesianRidge()],
           ['ElasticNet', ElasticNet()],
           ['HuberRegressor', HuberRegressor()]]

print("Results...")


for name,model in models:
    
    model = model
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    with open(name + '.pkl', 'wb') as file:  
        pickle.dump(model, file)
    print(name, (np.sqrt(mean_squared_error(y_test, predictions))))