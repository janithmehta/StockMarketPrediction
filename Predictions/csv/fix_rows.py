import pandas as pd 
import statistics as st
import numpy as np
list1=['AMBUJACEM','ASIANPAINT','BANKBARODA','HDIL','HEROMOTOCO','HINDUNILVR','ITC','INFY','TCS','MARUTI']
#list1=['AMBUJACEM']
for m in list1:
        name=m+'.csv'
        df=pd.read_csv(name)
        for i in range(len(df)-20,len(df)-1):
                df['Next Day Price'][i]=df['Close'][i+1]
        for i in range(len(df)-20,len(df)-5):
                df['5 Day Price'][i]=df['Close'][i+5]
        for i in range(len(df)-20,len(df)-10):
                df['10 Day Price'][i]=df['Close'][i+10]
        for i in range(len(df)-20,len(df)-15):
                df['15 Day Price'][i]=df['Close'][i+15]
        df.drop('Unnamed: 0', axis=1, inplace=True)
        df.to_csv(name)


