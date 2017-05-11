import os
from django.conf import settings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

def predict(company):
    #Enter the prediction here, you will be getting the company code as input Eg: TCS,INFY,HEROMOTOCO
    '''
    :param company: company code
    :return: list
    Output is a list with dictionaries
    Eg:
    [
    {'day':"Tomorrow", 'value':"58.55"},
    {'day':"5 days later", 'value':"58.55"},
    {'day':"10 days later", 'value':"58.55"},
    {'day':"15 days later", 'value':"58.55"},
    .
    .
    .
    .
    ]

    '''
    print("Company name"+company)
    #dict1={'AMBUJACEM':'.csv','INFY':'infosys2.csv'}
    FEATURES =['Close','X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16','X17','X18','X19','X20','X21','X22','X23','X24','M5','M10','M15','M20','One Day Momentum','Five Day Momentum','Ten Day Momentum','Fifteen Day Momentum','Twenty Day Momentum']
    #df = pd.DataFrame.from_csv(dict1[company])
    name=company+".csv"
    #df=pd.DataFrame.from_csv(name)
    df = pd.read_csv(name)
    #test_size = 200
    df=df.replace([np.inf,-np.inf],np.nan)
    df=df.replace('#DIV/0!',np.nan)
    df=df.dropna()
    predictions=[]
    list_index=['Next Day Price','5 Day Price','10 Day Price','15 Day Price','20 Day Price']
    for h in list_index:
        X = np.array(df[FEATURES].values)
        y = (df[h].values)
        reg=linear_model.Lasso(alpha=0.1)
        reg.fit(X[40:len(df)-20],y[40:len(df)-20])
        price=reg.predict(X[len(df)-1])[0]
        dict2={'day':"",'value':""}
        print(X[len(df)-1])
        dict2['day']=h
        dict2['value']=price
        predictions.append(dict2)

    print(predictions)
    '''
    predictions =  [
    {'day':"Tomorrow", 'value':"58.55"},
    {'day':"5 days later", 'value':"58.55"},
    {'day':"10 days later", 'value':"58.55"},
    {'day':"15 days later", 'value':"58.55"},
    ]
    '''
    return predictions

predict('AMBUJACEM')
