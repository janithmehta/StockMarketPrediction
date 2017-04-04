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
    # dict1={'AMB':'ambuja2.csv','INFY':'infosys2.csv'}
    # FEATURES =['Close','X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16','X17','X18','X19','X20','X21','X22','X23','X24','M5','M10','M15','M20','One Day Momentum','Five Day Momentum','Ten Day Momentum','Fifteen Day Momentum','Twenty Day Momentum']
    # df = pd.DataFrame.from_csv(dict1[company])
    # #test_size = 200
    # df=df.replace([np.inf,-np.inf],np.nan)
    # df=df.replace('#DIV/0!',np.nan)
    # df=df.dropna()
    # predictions=[]
    # list_index=['Next Day Price','5 Day Price','10 Day Price','15 Day Price','20 Day Price']
    # for h in list_index:
    #     X = np.array(df[FEATURES].values)
    #     y = (df[h].values)
    #     reg=linear_model.Lasso(alpha=0.1)
    #     reg.fit(X[0:len(df)-21],y[0:len(df)-21])
    #     price=reg.predict(X[len(df)-1])[0]
    #     dict2={'day':"",'value':""}
    #     dict2['day']=h
    #     dict2['value']=price
    #     predictions.append(dict2)
    #
    #
    #
    # print(predictions)


    print("Company name"+company)
    #dict1={'AMBUJACEM':'.csv','INFY':'infosys2.csv'}
    FEATURES =['Close','X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16','X17','X18','X19','X20','X21','X22','X23','X24','M5','M10','M15','M20','One Day Momentum','Five Day Momentum','Ten Day Momentum','Fifteen Day Momentum','Twenty Day Momentum']
    #df = pd.DataFrame.from_csv(dict1[company])
    name=company+".csv"
    #df=pd.DataFrame.from_csv(name)
    df = pd.read_csv(settings.MEDIA_ROOT + name)
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
        reg.fit(X[0:len(df)-21],y[0:len(df)-21])
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

def stock_prices(company):
    #return the list of stock prices and dates(in a dict), list of dicts
    # dict1={'AMB':'ambuja2.csv','INFY':'infosys2.csv'}
    name=company+'.csv'
    df = pd.DataFrame.from_csv(settings.MEDIA_ROOT + name)
    #test_size = 200
    df=df.replace([np.inf,-np.inf],np.nan)
    df=df.replace('#DIV/0!',np.nan)
    df=df.dropna()
    print(df.keys())
    #print(df['Date'][1])
    prices=[]
    for i in range(40,len(df)-1):
        dict2={'day':"",'value':""}
        dict2['day']=df['Date'][i]
        dict2['value']=df['Close'][i]
        prices.append(dict2)
    # print(prices)
    return prices

def company_latest(company):
    #details = {'name': "AMNUJA CEMENTS", 'price':"222.5", 'change': "+", 'change_price':"22.5"}
    details={'name':"",'price':"",'change':"","change_price":""}
    name=company+".csv"
    #df=pd.DataFrame.from_csv(name)
    df = pd.read_csv(settings.MEDIA_ROOT + name)
    #df=pd.DataFrame.from_csv("ambuja2.csv")
    df1=df.tail(1)
    x=df1.index[0]
    print(x)
    print(df['Date'][x])
    p1=df['Close'][x]
    p2=df['Close'][x-1]
    diff=p1-p2
    sign=""
    if(p1-p2>=0):
        sign="+"
    elif(p1-p2<0):
        sign="-"
    details['name']=company
    details['price']=p1
    details['change']=sign
    details['change_price']=diff
    return details

def plot(company):
    #dict1={'AMB':'ambuja2.csv','INFY':'infosys2.csv'}
    file_name = "csv/"+"ITC"+".csv"
    name=company+".csv"
    df = pd.read_csv(settings.MEDIA_ROOT + name)
    # print(df.keys())
    # print(settings.MEDIA_ROOT)
    # df=df.replace([np.inf,-np.inf],np.nan)
    # df=df.replace('#DIV/0!',np.nan)
    # df=df.dropna()
    # dates=[]
    # prices=[]
    # for i in range(40,len(df)):
    #
    #     dates.append(df['Date'][i])
    #     prices.append(df['Close'][i])
    # x = [dt.datetime.strptime(d,'%d-%m-%Y').date() for d in dates]
    # fig = plt.figure(1)
    # ax1 = fig.add_subplot(111)
    # ax1.plot(x,prices)
    # #plt.plot(x,prices)
    # #plt.show()
    # fig.savefig("prices.png")
    
    print("plot")

def recommend(amount):
    amount = int(amount)
    print(amount, type(amount))
    suggestions = [
        {'company_name':"AMBUJA", 'amount':'1000'},
        {'company_name':"AMBUJA", 'amount':'1000'},
        {'company_name':"AMBUJA", 'amount':'1000'}
    ]
    return suggestions
#predict("AMB")
#stock_prices("AMB")
# plot("AMBUJACEM")
#predict("AMBUJACEM")