def add(x,y):
    sum=x+y
    print(a," + ",b," = ",sum)
def sub(x,y):
    s=x-y
    print(a," - ",b," = ",s)
def mul(x,y):
    m=x*y
    print(a," * ",b," = ",m)
def div(x,y):
    d=x/y
    print(a," / ",b," = ",d)
def floor_div(x,y):
    d=x//y
    print(a," // ",b," = ",d)
print("Enter the Two Numbers : ")
a=int(input())
b=int(input())
print("Press + for Addition")
print("Press - for Subtraction")
print("Press * for multiplication")
print("Press / for Division")
print("Press // for Floor Division")
ch=input()
if(ch=='+'):
    add(a,b)
elif(ch=='-'):
    sub(a,b)
elif(ch=='*'):
    mul(a,b)
elif(ch=='/'):
    div(a,b)
elif(ch=='//'):
    floor_div(a,b)
else:
    print("Invalid Choice")




