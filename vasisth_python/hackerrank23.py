from itertools import product
num_1=list(map(int,input("").split(" ")))
num_2=list(map(int,input("").split(" ")))
num3=list(product(*[num_1,num_2]))
for i in num3:
    print(i,end="")