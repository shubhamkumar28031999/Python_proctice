import pandas as pd
import quandl,math
import numpy as np
from sklearn import preprocessing,svm
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['Hl_ptc']=(df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100
df['Hl_change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100
df=df[['Adj. Close','Hl_ptc','Hl_change','Adj. Volume']]
forecast_col='Adj. Close'
df.fillna(-9999.0,inplace=True)
forecast_out=int(math.ceil(0.01*len(df)))
df['label']=df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.tail())
x=np.array(df.drop(['label'],1))
y=np.array(df['label'])

x= preprocessing.scale(x)
y=np.array((df['label']))

x_train,x_test,_y_train,y_test =train_test_split(x,y,test_size=0.2)
clf=LinearRegression()
clf.fit(x_train,_y_train)
accuracy = clf.score(x_test,y_test)
print(accuracy)