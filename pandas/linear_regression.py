import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

data = pd.read_csv("housing_price.csv")
# print(data)
x=list(data.iloc[:,:-1].values)
y=list(data.iloc[:,1].values)
print(x)
# plt.scatter(x,y)
# plt.show()

x_train,x_text,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)
lr=LinearRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_text)

plt.scatter(x_train,y_train,color='blue')
plt.plot(x_train,lr.predict(x_train),color='red')
plt.show()

plt.scatter(x_text,y_test,color='green')
plt.plot(x_text,lr.predict(x_text),color='yellow')
plt.show()

print('MAE:', metrics.mean_absolute_error(y_test,y_pred))
print('MSE:',metrics.mean_squared_error(y_test,y_pred))
print("RMSE:",np.sqrt(metrics.mean_absolute_error(y_test,y_pred)))