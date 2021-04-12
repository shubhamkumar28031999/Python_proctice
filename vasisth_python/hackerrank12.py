import numpy as np
x,y=[int(x) for x in input("").split(" ")]
list1=[]
for i in range(0,x):
    list1.append(list(map(int,input("").split(" "))))
np.array(list1)
print(np.prod(np.sum(list1,axis=0)))