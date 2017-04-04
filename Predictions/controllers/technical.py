import os
from django.conf import settings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from sklearn import linear_model, preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

companies_list = [
        {'value':"AMBUJACEM", 'name':"Ambuja Cement"},
        {'value':"ASIANPAINT", 'name':"Asian Paints"},
        {'value':"BANKBARODA", 'name':"Bank Of Baroda"},
        {'value':"HDIL", 'name':"Housing Develoopment & Infrastructure Ltd."},
        {'value':"HEROMOTOCO", 'name':"Hero Motor Corporation"},
        {'value':"HINDUNILVR", 'name':"Hindustan Unilever"},
        {'value':"INFY", 'name':"Infosys"},
        {'value':"ITC", 'name':"ITC"},
        {'value':"MARUTI", 'name':"Maruti Suzuki Ltd."},
        {'value':"TCS", 'name':"Tata Consultancy Services"},
    ]


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
    if company == "ITC":

        predictions =  [
        {'day':"Tomorrow", 'value':"58.55"},
        {'day':"5 days later", 'value':"58.55"},
        {'day':"10 days later", 'value':"58.55"},
        {'day':"15 days later", 'value':"58.55"},
        {'day':"20 days later", 'value':"68.55"},
        ]
    else:
        predictions =  [
        {'day':"Tomorrow", 'value':"48.55"},
        {'day':"5 days later", 'value':"58.55"},
        {'day':"10 days later", 'value':"58.55"},
        {'day':"15 days later", 'value':"58.55"},
        {'day':"20 days later", 'value':"68.55"},
        ]
    return predictions

def stock_prices(company):
    #return the list of stock prices and dates(in a dict), list of dicts
    # dict1={'AMB':'ambuja2.csv','INFY':'infosys2.csv'}
    df = pd.DataFrame.from_csv(settings.MEDIA_ROOT + 'ITC.csv')
    #test_size = 200
    df=df.replace([np.inf,-np.inf],np.nan)
    df=df.replace('#DIV/0!',np.nan)
    df=df.dropna()
    print(df.keys())
    #print(df['Date'][1])
    prices=[]
    for i in range(40,len(df)):
        dict2={'day':"",'value':""}
        dict2['day']=df['Date'][i]
        dict2['value']=df['Close'][i]
        prices.append(dict2)
    # print(prices)
    return prices

def company_latest(company):
    details = {'name': "AMNUJA CEMENTS", 'price':"222.5", 'change': "+", 'change_price':"22.5"}
    return details

def plot(company):
    dict1={'AMB':'ambuja2.csv','INFY':'infosys2.csv'}
    file_name = "csv/"+"ITC"+".csv"
    df = pd.read_csv(settings.MEDIA_ROOT + 'ITC.csv')
    print(settings.STATICFILES_DIRS + "csv")
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
    price_change = []

    for commpany in companies_list:
        temp = {}
        predictions = predict(commpany['value'])
        twenty_day = float((predictions[4]['value']))
        next_day = float((predictions[0]['value']))
        temp['company'] = commpany['value']
        temp['change'] = twenty_day - next_day
        price_change.append(temp)

    sorted_price_change = sorted(price_change, key=lambda k: k['change'], reverse=True)

    initial_seed = float(amount)
    x_50=initial_seed*0.5
    x_30=initial_seed*0.3
    x_20=initial_seed*0.2

    suggestions = []

    if float(sorted_price_change[2]['change']) > 0:
        for c in companies_list:
            temp = {}
            if c['value'] == sorted_price_change[0]['company']:
                temp['company_name'] = c['name']
                temp['amount'] = x_50
                temp['profit'] = sorted_price_change[0]['change'] * x_50
                suggestions.append(temp)
            elif c['value'] == sorted_price_change[1]['company']:
                temp['company_name'] = c['name']
                temp['amount'] = x_30
                temp['profit'] = sorted_price_change[1]['change'] * x_30
                suggestions.append(temp)
            elif c['value'] == sorted_price_change[2]['company']:
                temp['company_name'] = c['name']
                temp['amount'] = x_20
                temp['profit'] = sorted_price_change[2]['change'] * x_20
                suggestions.append(temp)
    elif float(sorted_price_change[1]['change']) > 0 and float(sorted_price_change[2]['change']) <= 0:
        for c in companies_list:
            temp = {}
            if c['value'] == sorted_price_change[0]['company']:
                temp['company_name'] = c['name']
                temp['amount'] = x_50
                temp['profit'] = sorted_price_change[0]['change'] * x_50
                suggestions.append(temp)
            elif c['value'] == sorted_price_change[1]['company']:
                temp['company_name'] = c['name']
                temp['amount'] = x_30
                temp['profit'] = sorted_price_change[1]['change'] * x_30
                suggestions.append(temp)
    elif float(sorted_price_change[1]['change']) <= 0 and float(sorted_price_change[2]['change']) <= 0:
        for c in companies_list:
            temp = {}
            if c['value'] == sorted_price_change[0]['company']:
                temp['company_name'] = c['name']
                temp['amount'] = x_50
                temp['profit'] = sorted_price_change[0]['change'] * x_50
                suggestions.append(temp)
    elif float(sorted_price_change[0]['change']) < 0:
        temp = {}
        temp['company_name'] = "Don't Invest"
        temp['amount'] = 0
        temp['profit'] = "negative"
        suggestions.append(temp)

    return suggestions
