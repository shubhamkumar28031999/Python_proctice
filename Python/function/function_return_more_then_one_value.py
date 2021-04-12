def swap(x,y):
    temp=x
    x=y
    y=temp
    return x,y
print("Enter the Two Numbers : ")
a=int(input())
b=int(input())
print("Before Calling Swap function a = ",a," and b = ",b)
a,b=swap(a,b)
print("After Calling Swap function a = ",a," and b = ",b)
input()
