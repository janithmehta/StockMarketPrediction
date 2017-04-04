from django.conf import settings

import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, preprocessing
import pandas as pd
from matplotlib import style
style.use("ggplot")
import warnings
warnings.filterwarnings("ignore")
import csv

def predict(company):
    #Enter the prediction here, you will be getting the company code as input Eg: TCS,INFY,HEROMOTOCO
    #Output 1 or 0. 1-Good, 0-Bad
    FEATURES =  ['basic_eps',
             'book_value_excl_per_share',
             'dividend_per_share',
             'revenue_per_share',
             'pbdit_per_share',
             'net_profit_per_share',
             'pbdit_margin',
             'net_profit_margin',
             #'return_on_assets',
             'debt_by_equity',
             'asset_turnover_ratio',
             'current_ratio',
             'dividend_payout_ratio',
             'price_per_bv',
             'price_by_net_revenue',
             'ev_by_ebita',
             'ev_by_net_operating_revenue',
             'market_cap_by_net_operating_revenue']
             #'retention_ratios']
    data_df = pd.DataFrame.from_csv("xyzc2.csv")
    X = np.array(data_df[FEATURES].values)
    y = (data_df["status"].values)
    X = preprocessing.scale(X)
    #test_size=100
    #print(len(X))
    time.sleep(0.25)
    #company =input("Enter Company Name : ")
    company1 = company.lower()
    company2 = company.upper()
    company3 = company.title()
    with open(settings.MEDIA_ROOT + 'fundamental.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        year = []
        for row in reader:
            if row['company'] == company or row['company'] == company1 or row['company'] == company2 or row['company'] == company3:
                year.append(row['year'])

        length =  len(year)
        max_year = max(year)
        ratios = []
        with open(settings.MEDIA_ROOT + 'fundamental.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if ((row['company'] == company or row['company'] == company1 or row['company'] == company2 or row['company'] == company3) and row['year'] == max_year):
                    ratios.append(row['basic_eps'])
                    ratios.append(row['book_value_excl_per_share'])
                    ratios.append(row['dividend_per_share'])
                    ratios.append(row['revenue_per_share'])
                    ratios.append(row['pbdit_per_share'])
                    ratios.append(row['net_profit_per_share'])
                    ratios.append(row['pbdit_margin'])
                    ratios.append(row['net_profit_margin'])
                    #ratios.append(row['return_on_assets'])
                    ratios.append(row['debt_by_equity'])
                    ratios.append(row['asset_turnover_ratio'])
                    ratios.append(row['current_ratio'])
                    ratios.append(row['dividend_payout_ratio'])
                    ratios.append(row['price_per_bv'])
                    ratios.append(row['price_by_net_revenue'])
                    ratios.append(row['ev_by_ebita'])
                    ratios.append(row['ev_by_net_operating_revenue'])
                    ratios.append(row['market_cap_by_net_operating_revenue'])
                    #ratios.append(row['retention_ratios'])
    #print(ratios)
    clf = svm.SVC(kernel="linear", C=1)

    #print("1")
    #clf.fit(X[:-test_size],y[:-test_size])
    #print("2")
    clf.fit(X,y)
    #asian paints
    #print(clf.predict([16.65,51.74,7.5,131.84,28.20,16.65,21.38,0.01,151.19,1.47,45.03,16.79,6.59,30.76,6.58,6.59]))
    if clf.predict(ratios):
        return 0
    else:
        return 1
    #print(clf.coef_)
    #print(clf.intercept_)
    # correct_count = 0
    #for x in range(1, test_size+1):
    #    if clf.predict(X[-x])[0] == y[-x]:
    #        correct_count += 1

    #print("Accuracy:", (correct_count/test_size) * 100.00)