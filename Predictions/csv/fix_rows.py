import pandas as pd 
import statistics as st
import numpy as np
list1=['AMBUJACEM','ASIANPAINT','BANKBARODA','HDIL','HEROMOTOCO','HINDUNILVR','ITC','INFY','TCS','MARUTI']
for m in list1:
        name=m+'.csv'
        df=pd.read_csv(name)
        #df=df[::-1]
        #For Old format
        '''
        df=df.replace([np.inf,-np.inf],np.nan)
        df=df.replace('#DIV/0!',np.nan)
        df=df.replace('null',np.nan)
        df=df.dropna()
        df['X1'] = 0.00
        df['X2'] = 0.00
        df['X3'] = 0.00
        df['X4'] = 0.00
        df['X5'] = 0.00
        df['X6'] = 0.00
        df['X7'] = 0.00
        df['X8'] = 0.00
        df['X9'] = 0.00
        df['X10'] = 0.00
        df['X11'] = 0.00
        df['X12'] = 0.00
        df['X13'] = 0.00
        df['X14'] = 0.00
        df['X15'] = 0.00
        df['X16']=0.00
        df['X17']=0.00
        df['X18']=0.00
        df['X19']=0.00
        df['X20']=0.00
        df['X21']=0.00
        df['X22']=0.00
        df['X23']=0.00
        df['X24']=0.00
        df['K5']=0.00
        df['K10']=0.00
        df['K15']=0.00
        df['K20']=0.00
        df['M1']=0.00
        df['M5']=0.00
        df['M10']=0.00
        df['M15']=0.00
        df['M20']=0.00
        df['One Day Momentum']=0.00
        df['Five Day Momentum']=0.00
        df['Ten Day Momentum']=0.00
        df['Fifteen Day Momentum']=0.00
        df['Twenty Day Momentum']=0.00
        df['Next Day Price']=0.00
        df['5 Day Price']=0.00
        df['10 Day Price']=0.00
        df['15 Day Price']=0.00
        df['20 Day Price']=0.00
        df['One Day Change']=0.00
        df['Five Day Change']=0.00
        df['Ten Day Change']=0.00
        df['Fifteen Day Change']=0.00
        df['Twenty Day Change']=0.00
        df['One Day Trend']=0.00
        df['Five Day Trend']=0.00
        df['Ten Day Trend']=0.00
        df['Fifteen Day Trend']=0.00
        df['Twenty Day Trend']=0.00
        df['Close']=df['Close'].astype(float)
        df['High']=df['High'].astype(float)
        df['Low']=df['Low'].astype(float)
        '''
        for i in range(len(df)-20,len(df)):
                '''
                df['X1'][i]=(df['Close'][i]-df['Close'][i-1])/df['Close'][i-1]

                ma5=0.0
                for j in range(1,6):
                        ma5+=df['Close'][i-j]
                ma5=ma5/5

                df['X2'][i]=(df['Close'][i]-ma5)/ma5

                ma10=0.0
                for j in range(1,11):
                        ma10+=df['Close'][i-j]
                ma10=ma10/10

                df['X3'][i]=(df['Close'][i]-ma10)/ma10


                ma15=0.0
                for j in range(1,16):
                        ma15+=df['Close'][i-j]
                ma15=ma15/15

                df['X4'][i]=(df['Close'][i]-ma15)/ma15

                ma20=0.0
                for j in range(1,21):
                        ma20+=df['Close'][i-j]
                ma20=ma20/20

                df['X5'][i]=(df['Close'][i]-ma20)/ma20

                ma25=0.0
                for j in range(1,26):
                        ma25+=df['Close'][i-j]
                ma25=ma25/25

                df['X6'][i]=(df['Close'][i]-ma25)/ma25

                ma30=0.0
                for j in range(1,31):
                        ma30+=df['Close'][i-j]
                ma30=ma30/30

                df['X7'][i]=(df['Close'][i]-ma30)/ma30

                ma35=0.0
                for j in range(1,36):
                        ma35+=df['Close'][i-j]
                ma35=ma35/35

                df['X8'][i]=(df['Close'][i]-ma35)/ma35

                ma40=0.0
                for j in range(1,41):
                        ma40+=df['Close'][i-j]
                ma40=ma40/40

                df['X9'][i]=(df['Close'][i]-ma40)/ma40

                ub10=0.0
                #print(df['Close'][i-1:i-11])
                ub10=ma10+0.02*st.pstdev(df['Close'][i-11:i-1])

                lb10=0.0
                lb10=ma10-0.02*st.pstdev(df['Close'][i-11:i-1])

                ub20=0.0
                ub20=ma20+0.02*st.pstdev(df['Close'][i-21:i-1])

                lb20=0.0
                lb20=ma20-0.02*st.pstdev(df['Close'][i-21:i-1])

                ub30=0.0
                ub30=ma30+0.02*st.pstdev(df['Close'][i-31:i-1])

                lb30=0.0
                lb30=ma30-0.02*st.pstdev(df['Close'][i-31:i-1])
                

                if df['Close'][i]>ub10:
                        df['X10'][i]=df['Close'][i]-ub10
                elif df['Close'][i]<lb10:
                        df['X10'][i]=df['Close'][i]-lb10

                if df['Close'][i]>ub20:
                        df['X11'][i]=df['Close'][i]-ub20
                elif df['Close'][i]<lb20:
                        df['X11'][i]=df['Close'][i]-lb20

                if df['Close'][i]>ub30:
                        df['X12'][i]=df['Close'][i]-ub30
                elif df['Close'][i]<lb30:
                        df['X12'][i]=df['Close'][i]-lb30

                rs5=0.0
                change=0.0
                gain=0.0
                loss=0.0
                for j in range(0,5):
                        change=df['Close'][i-j]-df['Close'][i-j-1]
                        if change>0.0:
                                gain+=change
                        elif change<0.0:
                                loss+=(-1*change)

                if loss==0.0:
                        rsi5=100.0
                else:
                        rs5=gain/loss
                        rsi5=0.0
                        rsi5=100.0-100.0/(1+rs5)

                df['X13'][i]=(rsi5-50.0)/50.0

                rs10=0.0
                change=0.0
                gain=0.0
                loss=0.0
                for j in range(0,10):
                        change=df['Close'][i-j]-df['Close'][i-j-1]	
                        if change>0.0:
                                gain+=change
                        elif change<0.0:
                                loss+=(-1*change)

                if loss==0.0:
                        rsi10=100
                else:
                        rs10=gain/loss
                        rsi10=0.0
                        rsi10=100.00-100.00/(1+rs10)
                
                df['X14'][i]=(rsi10-50.00)/50.00

                rs15=0.0
                change=0.0
                gain=0.0
                loss=0.0
                for j in range(0,15):
                        change=df['Close'][i-j]-df['Close'][i-j-1]
                        if change>0.0:
                                gain+=change
                        elif change<0.0:
                                loss+=(-1*change)

                if loss==0.0:
                        rsi15=100.00
                else:
                        rs15=gain/loss
                        rsi15=0.0
                        rsi15=100.00-100.00/(1+rs15)

                df['X15'][i]=(rsi15-50.00)/50.00

                rs20=0.0
                change=0.0
                gain=0.0
                loss=0.0
                for j in range(0,20):
                        change=df['Close'][i-j]-df['Close'][i-j-1]
                        if change>0.0:
                                gain+=change
                        elif change<0.0:
                                loss+=(-1*change)

                if loss==0.0:
                        rsi20=100.00
                else:
                        rs20=gain/loss
                        rsi20=0.0
                        rsi20=100.00-100.00/(1+rs20)

                df['X16'][i]=(rsi20-50.00)/50.00

                min_low_price=1000000
                max_high_price=0
                for j in range(1,6):
                        min_low_price=min(min_low_price,df['Low'][i-j])
                        max_high_price=max(max_high_price,df['High'][i-j])

                k5=100*((df['Close'][i]-min_low_price)/(max_high_price-min_low_price))

                df['K5'][i] = k5
                df['X17'][i]=(k5-50)/50

                min_low_price=1000000
                max_high_price=0
                for j in range(1,11):
                        min_low_price=min(min_low_price,df['Low'][i-j])
                        max_high_price=max(max_high_price,df['High'][i-j])

                k10=100*((df['Close'][i]-min_low_price)/(max_high_price-min_low_price))

                df['K10'][i] = k10
                df['X18'][i]=(k10-50)/50

                min_low_price=1000000
                max_high_price=0
                for j in range(1,16):
                        min_low_price=min(min_low_price,df['Low'][i-j])
                        max_high_price=max(max_high_price,df['High'][i-j])

                k15=100*((df['Close'][i]-min_low_price)/(max_high_price-min_low_price))

                df['K15'][i]=k15
                df['X19'][i]=(k15-50)/50

                min_low_price=1000000
                max_high_price=0
                for j in range(1,21):
                        min_low_price=min(min_low_price,df['Low'][i-j])
                        max_high_price=max(max_high_price,df['High'][i-j])

                k20=100*((df['Close'][i]-min_low_price)/(max_high_price-min_low_price))

                df['K20'][i]=k20
                df['X20'][i]=(k20-50)/50

                #Newly added Code on 22/1/17
                #new code 21/2/17
                '''
                if(i-1>-1):
                        df['Next Day Price'][i]=df['Close'][i+1]

                if(i-5>-1):
                        df['5 Day Price'][i]=df['Close'][i+5]

                if(i-10>-1):
                        df['10 Day Price'][i]=df['Close'][i+10]

                if(i-15>-1):
                        df['15 Day Price'][i]=df['Close'][i+15]

                if(i-20>-1):
                        df['20 Day Price'][i]=df['Close'][i+20]
                '''

                df['M1'][i]=(df['Close'][i]-df['Close'][i-1])/(df['Close'][i-1])

                df['M5'][i]=(df['Close'][i]-df['Close'][i-5])/(df['Close'][i-5])

                df['M10'][i]=(df['Close'][i]-df['Close'][i-10])/(df['Close'][i-10])

                df['M15'][i]=(df['Close'][i]-df['Close'][i-15])/(df['Close'][i-15])

                df['M20'][i]=(df['Close'][i]-df['Close'][i-20])/(df['Close'][i-20])

                if df['M1'][i]>0:
                        df['One Day Momentum'][i]=1
                else:
                        df['One Day Momentum'][i]=-1

                if df['M5'][i]>0:
                        df['Five Day Momentum'][i]=1
                else:
                        df['Five Day Momentum'][i]=-1

                if df['M10'][i]>0:
                        df['Ten Day Momentum'][i]=1
                else:
                        df['Ten Day Momentum'][i]=-1

                if df['M15'][i]>0:
                        df['Fifteen Day Momentum'][i]=1
                else:
                        df['Fifteen Day Momentum'][i]=-1

                if df['M20'][i]>0:
                        df['Twenty Day Momentum'][i]=1
                else:
                        df['Twenty Day Momentum'][i]=-1

                df['One Day Change'][i]=(df['Close'][i-1]-df['Close'][i])/(df['Close'][i])

                if df['One Day Change'][i]>0:
                        df['One Day Trend'][i]=1
                else:
                        df['One Day Trend'][i]=-1

                df['Five Day Change'][i]=(df['Close'][i-5]-df['Close'][i])/(df['Close'][i])

                if df['Five Day Change'][i]>0:
                        df['Five Day Trend'][i]=1
                else:
                        df['Five Day Trend'][i]=-1

                df['Ten Day Change'][i]=(df['Close'][i-10]-df['Close'][i])/(df['Close'][i])

                if df['Ten Day Change'][i]>0:
                        df['Ten Day Trend'][i]=1
                else:
                        df['Ten Day Trend'][i]=-1

                df['Fifteen Day Change'][i]=(df['Close'][i-15]-df['Close'][i])/(df['Close'][i])

                if df['Fifteen Day Change'][i]>0:
                        df['Fifteen Day Trend'][i]=1
                else:
                        df['Fifteen Day Trend'][i]=-1

                df['Twenty Day Change'][i]=(df['Close'][i-20]-df['Close'][i])/(df['Close'][i])

                if df['Twenty Day Change'][i]>0:
                        df['Twenty Day Trend'][i]=1
                else:
                        df['Twenty Day Trend'][i]=-1

                print("Loop1")


        for i in range(len(df)-20,len(df)):

                d5=0.0
                for j in range(1,6):
                        d5+=df['K5'][i-j]
                d5=d5/5
                df['X21'][i]=(df['K5'][i]-d5-50)/50

                d10=0.0
                for j in range(1,11):
                        d10+=df['K10'][i-j]
                d10=d10/10
                df['X22'][i]=(df['K10'][i]-d10-50)/50

                d15=0.0
                for j in range(1,16):
                        d15+=df['K15'][i-j]
                d15=d15/15
                df['X23'][i]=(df['K15'][i]-d15-50)/50

                d20=0.0
                for j in range(1,21):
                        d20+=df['K20'][i-j]
                d20=d20/20
                df['X24'][i]=(df['K20'][i]-d20-50)/50
                print("loop2")

        #df=df.ix[20:]
        #df=df.ix[:-20]
        #df=df.drop(df.index[0:41])
        #df=df.drop(df.index[790:len(df['Date'])])
        df.drop('Unnamed: 0', axis=1, inplace=True)
        df.to_csv(name)


