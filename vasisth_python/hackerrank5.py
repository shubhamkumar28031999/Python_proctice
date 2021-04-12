def func(lst,age):
    return lst.count(max(lst))

age=int(input(""))
lst=list(map(int,input().strip().split(" ")))
x=func(lst,age)
print(x)