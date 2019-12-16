from flask import Flask,request,make_response,Response
from flask import jsonify 
import json
import pickle
import numpy as np 
import pandas as pd
from flask_cors import CORS, cross_origin

models = ['DecisionTree',
           'Linear Regression', 
           'RandomForest',
           'KNeighbours',
           'SVM',
           'AdaBoostClassifier',
           'GradientBoostingClassifier',
           
           'Lasso',
           'Ridge',
           'BayesianRidge',
           'ElasticNet',
           'HuberRegressor']

preDict = {}

for model in models:
    loaded_model= pickle.load(open(model+'.pkl', 'rb'))
    preDict[model] = loaded_model

x_test = np.array([337,118,4,4.5,4.5,9.65,1]).reshape(1,-1)

print(preDict)
print(x_test)

app = Flask(__name__)
result = {}
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/predict',methods = ['POST'])
@cross_origin()
def send_pred():
    req= request.get_json(force = True)
    x_test = []
    for key in req:
        print(req[key])
        x_test.append(float(req[key]))
    x_test = np.array(x_test).reshape(1,-1)
    print(x_test)
    pred = preDict['DecisionTree'].predict(x_test).tolist()
    result['first'] = json.dumps(pred[0])
    return  Response(json.dumps(result), mimetype='application/json') 
    
app.run()