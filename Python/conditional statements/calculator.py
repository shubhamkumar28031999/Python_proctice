print("Enter the Two Numbers :  ")
a=int(input())
b=int(input())
print("Press + for Addition")
print("Press - for Subtraction")
print("Press * for Multiplicatin")
print("Press / for Division")
print("Press // for Division(Floor Value)")
ch=input("Enter Your Choice :  ")
if(ch=='+'):
	print(a," + ",b," = ",a+b)
elif(ch=='-'):
	print(a," - ",b," = ",a-b)
elif(ch=='*'):
	print(a," * ",b," = ",a*b)
elif(ch=='/'):
	print(a," / ",b," = ",a/b)
elif(ch=='//'):
	print(a," // ",b," = ",a//b)
else:
	print("Invalid Choice")
input()