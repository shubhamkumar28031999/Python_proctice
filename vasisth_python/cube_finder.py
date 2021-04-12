def fun(num):
    x={}
    for i in range(1,num+1):
        x[i]=i**3
    return x


num=int(input("enter any number"))
cubes=fun(num)
print(cubes)