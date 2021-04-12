from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

digits=load_digits()

# print(digits)

print('image Data Shape',digits.data.shape)
print('label Data Shape',digits.data.shape)

plt.figure(figsize=(20,4))
for index , (image,label) in enumerate(zip(digits.data[0:5],digits.target[0:5])):
    plt.subplot(1,5,index+1)
    plt.imshow(np.reshape(image,(8,8)),cmap=plt.cm.gray)
    plt.title('traing:%i \n ' %label, fontsize=20)
    plt.show()

x_train,x_test,y_train,y_test=train_test_split(digits.data,digits.target,test_size=0.25,random_state=0)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

logreg=LogisticRegression()
logreg.fit(x_train,y_train)

print(logreg.predict(x_test[0].reshape(1,-1)))

print(logreg.predict(x_test[0:10]))
prediction=logreg.predict((x_test))
score=logreg.score(x_test,y_test)
print(score)

