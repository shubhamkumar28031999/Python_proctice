class Sample:
    def __init__(self,a):
        self.a=a
    def __getitem__(self,i):
        return self.a[i]
x=[10,20,30,40,50,60,70,80,90,100]
obj=Sample(x)
print("List Using Object is :  ")
for i in range(0,10):
    print(obj[i],end=" ")
input()
